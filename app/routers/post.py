
from typing import List

from fastapi import (APIRouter, Depends, FastAPI, HTTPException, Response,
                     status)
from sqlalchemy.orm import Session

from .. import models, oauth2, schemas
from ..database import get_db

router = APIRouter(prefix="/posts",
                    tags=["posts"])

@router.get("/",response_model=list[schemas.Post])
def get_posts(db: Session = Depends(get_db)):
    # cursor.execute(""" SELECT * FROM posts """)
    # posts=cursor.fetchall()
    # print(posts)
    posts = db.query(models.Post, func.count(models.Vote.post_id).label("votes")).join(
        models.Vote, models.Vote.post_id == models.Post.id, isouter=True).group_by(models.Post.id).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()
    return posts
 


@router.post("/", status_code=status.HTTP_201_CREATED,response_model=schemas.Post)
def create_post(post: schemas.PostCreate,db: Session = Depends(get_db),current_user :int = Depends(oauth2.get_current_user)):
    # cursor.execute(""" INSERT into posts (title,content,published) VALUES (%s,%s,%s) RETURNING * """,
    #                 (post.title,post.content,post.published))
    # new_post = cursor.fetchall()
    # conn.commit()
    
    new_post = models.Post(owner_id=current_user.id,**post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


@router.get("/{id}",response_model=schemas.Post)
def get_post(id : int, responce : Response,db: Session = Depends(get_db)):
    # cursor.execute("""SELECT * FROM posts WHERE id = %s""", (str(id),))
    # post=cursor.fetchone()
    post = db.query(models.Post, func.count(models.Vote.post_id).label("votes")).join(
        models.Vote, models.Vote.post_id == models.Post.id, isouter=True).group_by(models.Post.id).filter(models.Post.id == id).first()
    if not post:
        # responce.status_code = status.HTTP_404_NOT_FOUND
        # return {"message":f"post with id:{id} not found"}
        raise HTTPException(status_code =  status.HTTP_404_NOT_FOUND,
        detail=f"post with id {id} not found")
    return  post


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int,db: Session = Depends(get_db),current_user :int = Depends(oauth2.get_current_user)):
    # cursor.execute("""DELETE FROM posts WHERE id = %s RETURNING * """, (str(id),))
    # deleted_post = cursor.fetchone()
    # conn.commit()
    post_query = db.query(models.Post).filter(models.Post.id ==id)

    post = post_query.first()
    if post ==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail=f"post with id: {id} does not exist")
    if post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail=f"not authorized to perform action")

    post_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)



@router.put("/{id}",status_code=status.HTTP_202_ACCEPTED,response_model=schemas.Post)
def update_post(id: int, updated_post: schemas.PostCreate,db: Session = Depends(get_db),current_user :int = Depends(oauth2.get_current_user)):
    # cursor.execute("""UPDATE posts set title = %s, content=%s,published=%s WHERE id = %s RETURNING *""",
    # (post.title,post.content,post.published,str(id)))
    # updated_post=cursor.fetchone()
    # conn.commit()
    post_query = db.query(models.Post).filter(models.Post.id==id)
    
    post = post_query.first()

    if post==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail=f"post with id : {id} is updated")

    if post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail=f"not authorized to perform action")


    post_query.update(updated_post.dict(),synchronize_session=False)
    db.commit()
    return  post_query.first()
