#!/usr/bin/env python3
from db.base_model import Base
from datetime import datetime
from sqlalchemy.sql import func
from sqlalchemy import DateTime, String, ForeignKey, Table, Column
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship
import uuid


blog_tags = Table(
    "blog_tags",
    Base.metadata,
    Column(
        "blog_id", UUID, ForeignKey("blogs.id", ondelete="CASCADE")
    ),  # blogs.id = BlogModel(tablename).id
    Column(
        "tag_id", UUID, ForeignKey("tags.id", ondelete="CASCADE")
    ),  # tags.id = TagModel(tablename).id
)


class TagModel(Base):
    __tablename__ = "tags"
    id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    name: Mapped[str] = mapped_column(String(length=60), default="")
    blogs: Mapped[list["BlogModel"]] = relationship(
        "BlogModel", secondary=blog_tags, passive_deletes=True
    )


class CategoryModel(Base):
    __tablename__ = "categories"
    id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    name: Mapped[str] = mapped_column(String(length=60), default="")
    blogs: Mapped[list["BlogModel"]] = relationship(
        "BlogModel",
        back_populates="category",  # BlogModel.category
    )


class BlogModel(Base):
    __tablename__ = "blogs"
    id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    title: Mapped[str] = mapped_column(String(length=160), default="")
    category_id: Mapped[UUID] = mapped_column(UUID, ForeignKey("categories.id"))
    category: Mapped["CategoryModel"] = relationship(
        "CategoryModel", back_populates="blogs", cascade="all, delete"
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=func.now()
    )
    tags: Mapped[list["TagModel"]] = relationship(
        "TagModel",
        secondary=blog_tags,
        back_populates="blogs",  # TagModel.blogs
        cascade="all, delete",
    )
