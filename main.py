from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Car, Bet
from schema import CarListValidate, CarBetValidate
from typing import List


app = FastAPI(title='Car auction')


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post('/car/create/', response_model=CarListValidate)
def create_car(car: CarListValidate, db: Session = Depends(get_db)):
    db_car = Car(**car.dict())
    db.add(db_car)
    db.commit()
    db.refresh(db_car)
    return db_car

@app.get('/cars/', response_model=List[CarListValidate])
def read_cars(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    cars = db.query(Car).offset(skip).limit(limit).all()
    return cars

@app.get('/cars/{car_id}', response_model=CarListValidate)
def read_car(car_id: int, db: Session = Depends(get_db)):
    car = db.query(Car).filter(Car.id == car_id).first()
    if car is None:
        raise HTTPException(status_code=404, detail='Car not found')
    else:
        return car

@app.put('/cars/update/{car_id}', response_model=CarListValidate)
def update_car(car_id: int, car: CarListValidate, db: Session = Depends(get_db)):
    db_car = db.query(Car).filter(Car.id == car_id).first()
    if db_car is None:
        raise HTTPException(status_code=404, detail='Car is not found')

    for key, value in car.dict().items():
        setattr(db_car, key, value)

    db.commit()
    db.refresh(db_car)
    return db_car

@app.delete('/cars/delete/{car_id}', response_model=CarListValidate)
def delete_car(car_id: int, db: Session = Depends(get_db)):
    db_car = db.query(Car).filter(Car.id == car_id).first()

    if db_car is None:
        raise HTTPException(status_code=404, detail='Car is not found')

    db.delete(db_car)
    db.commit()
    return db_car

@app.post('/bet/create/', response_model=CarBetValidate)
def create_car_bet(bet: CarBetValidate, db: Session = Depends(get_db)):
    db_bet = Bet(**bet.dict())
    db.add(db_bet)
    db.commit()
    db.refresh(db_bet)
    return db_bet












