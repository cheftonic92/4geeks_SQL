from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, ForeignKey, Integer, Float
from sqlalchemy.orm import Mapped, mapped_column, relationship

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'user'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    email: Mapped[str] = mapped_column(
        String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)
    favorites: Mapped[list["Favorite"]] = relationship(
        back_populates="user", cascade="all, delete-orphan")

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }


class Character(db.Model):
    __tablename__ = 'character'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False)
    uid: Mapped[int] = mapped_column(Integer, nullable=False)
    name: Mapped[str] = mapped_column(String(250), nullable=False)
    url: Mapped[str] = mapped_column(String(250))
    image: Mapped[str] = mapped_column(String(250))
    description: Mapped[str] = mapped_column(String(250))
    gender: Mapped[str] = mapped_column(String(250))
    eye_color: Mapped[str] = mapped_column(String(250))
    skin_color: Mapped[str] = mapped_column(String(250))
    hair_color: Mapped[str] = mapped_column(String(250))
    height: Mapped[float] = mapped_column(Float)
    mass: Mapped[float] = mapped_column(Float)
    homeworld: Mapped[str] = mapped_column(String(250))
    favorites: Mapped[list["Favorite"]] = relationship(
        back_populates="character", cascade="all, delete-orphan")

    def serialize(self):
        return {
            "id": self.id,
            "uid": self.uid,
            "name": self.name,
            "url": self.url,
            "image": self.image,
            "description": self.description,
            "gender": self.gender,
            "eye_color": self.eye_color,
            "skin-color": self.skin_color,
            "hair_color": self.hair_color,
            "height": self.height,
            "mass": self.mass,
            "homeworld": self.homeworld,
        }


class Planet(db.Model):
    __tablename__ = 'planet'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    uid: Mapped[int] = mapped_column(Integer, nullable=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    url: Mapped[str] = mapped_column(String(250))
    image: Mapped[str] = mapped_column(String(250))
    description: Mapped[str] = mapped_column(String(500))
    climate: Mapped[str] = mapped_column(String(100))
    terrain: Mapped[str] = mapped_column(String(100))
    population: Mapped[str] = mapped_column(String(100))
    diameter: Mapped[str] = mapped_column(String(100))
    rotation_period: Mapped[str] = mapped_column(String(100))
    orbital_period: Mapped[str] = mapped_column(String(100))
    gravity: Mapped[str] = mapped_column(String(100))
    surface_water: Mapped[str] = mapped_column(String(100))

    favorites: Mapped[list["Favorite"]] = relationship(
        back_populates="planet", cascade="all, delete-orphan")

    def serialize(self):
        return {
            "id": self.id,
            "uid": self.uid,
            "name": self.name,
            "url": self.url,
            "image": self.image,
            "description": self.description,
            "climate": self.climate,
            "terrain": self.terrain,
            "population": self.population,
            "diameter": self.diameter,
            "rotation_period": self.rotation_period,
            "orbital_period": self.orbital_period,
            "gravity": self.gravity,
            "surface_water": self.surface_water
        }


class Vehicle(db.Model):
    __tablename__ = 'vehicle'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    uid: Mapped[int] = mapped_column(Integer, nullable=False)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    url: Mapped[str] = mapped_column(String(250))
    image: Mapped[str] = mapped_column(String(250))
    description: Mapped[str] = mapped_column(String(500))
    model: Mapped[str] = mapped_column(String(100))
    manufacturer: Mapped[str] = mapped_column(String(100))
    cost_in_credits: Mapped[str] = mapped_column(String(100))
    max_atmosphering_speed: Mapped[str] = mapped_column(String(100))
    crew: Mapped[str] = mapped_column(String(100))
    passengers: Mapped[str] = mapped_column(String(100))
    cargo_capacity: Mapped[str] = mapped_column(String(100))
    consumables: Mapped[str] = mapped_column(String(100))

    favorites: Mapped[list["Favorite"]] = relationship(
        back_populates="vehicle", cascade="all, delete-orphan")

    def serialize(self):
        return {
            "id": self.id,
            "uid": self.uid,
            "name": self.name,
            "url": self.url,
            "image": self.image,
            "description": self.description,
            "model": self.model,
            "manufacturer": self.manufacturer,
            "cost_in_credits": self.cost_in_credits,
            "max_atmosphering_speed": self.max_atmosphering_speed,
            "crew": self.crew,
            "passengers": self.passengers,
            "cargo_capacity": self.cargo_capacity,
            "consumables": self.consumables
        }


class Favorite(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    character_id: Mapped[int] = mapped_column(
        ForeignKey("character.id"), nullable=True)
    planet_id: Mapped[int] = mapped_column(
        ForeignKey("planet.id"), nullable=True)
    vehicle_id: Mapped[int] = mapped_column(
        ForeignKey("vehicle.id"), nullable=True)

    user: Mapped["User"] = relationship(back_populates="favorites")
    character: Mapped["Character"] = relationship(back_populates="favorites")
    planet: Mapped["Planet"] = relationship(back_populates="favorites")
    vehicle: Mapped["Vehicle"] = relationship(back_populates="favorites")

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "character_id": self.character_id,
            "planet_id": self.planet_id,
            "vehicle_id": self.vehicle_id
        }
