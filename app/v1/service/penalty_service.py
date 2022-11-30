from fastapi import HTTPException, status

from app.v1.schema import penalty_schema
from app.v1.models.penalty_model import Penalty as PenaltyModel
from app.v1.models.lending_model import Lending as LendingModel


def add_penalty(penalty: penalty_schema.Penalty):

    db_penalty = PenaltyModel(
        days_late = penalty.days_late,
        total_taxes = penalty.total_taxes,
        state = penalty.state,
        lending_id = penalty.lending_id,
        created_at = penalty.created_at
    )

    db_penalty.save()

    return penalty_schema.Penalty(
        id = db_penalty.id,
        days_late = penalty.days_late,
        total_taxes = penalty.total_taxes,
        state = penalty.state,
        lending_id = penalty.lending_id,
        created_at = penalty.created_at,
    )

def get_penalties():

    """ if(is_done is None):
        tasks_by_user = PenaltyModel.filter(PenaltyModel.user_id == user.id).order_by(PenaltyModel.created_at.desc())
    else:
        tasks_by_user = PenaltyModel.filter((PenaltyModel.user_id == user.id) & (PenaltyModel.is_done == is_done)).order_by(PenaltyModel.created_at.desc()) """
    penalties = PenaltyModel.filter(PenaltyModel.lending_id == PenaltyModel.id).order_by(PenaltyModel.created_at.desc())

    list_penalties = []
    for penalty in penalties:
        list_penalties.append(penalty_schema.Penalty(
                id = penalty.id,
                days_late = penalty.days_late,
                total_taxes = penalty.total_taxes,
                state = penalty.state,
                lending_id = penalty.lending_id.id,
                created_at = penalty.created_at,
            )
        )

    return list_penalties

def get_penalty(penalty_id: int):
    penalty = PenaltyModel.filter((PenaltyModel.id == penalty_id)).first()

    if not penalty:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Penalty not found"
        )

    return penalty_schema.Penalty(
        id = penalty.id,
        days_late = penalty.days_late,
        total_taxes = penalty.total_taxes,
        state = penalty.state,
        lending_id = penalty.lending_id.id,
        created_at = penalty.created_at,
    )

def get_penalties_by_user_id(user_id: int):

    lendings_by_user_id = LendingModel.filter(LendingModel.user_id == user_id).order_by(LendingModel.created_at.desc())

    print("lendings_by_user_id",lendings_by_user_id)

    list_lendings_by_user_id = []
    for lending in lendings_by_user_id:
        print("lendingId",lending.id)
        list_lendings_by_user_id.append(PenaltyModel.filter((PenaltyModel.lending_id.id == lending.id)).order_by(LendingModel.created_at.desc()))
        
    print("list_lendings_by_user_id", list_lendings_by_user_id[0])    




    #penalties = 
    """ print(penalties)
    if not penalties:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Penalty not found"
        ) """

    list_penalties = []
    for penalty in list_lendings_by_user_id:
        print("penaltyId", penalty)
        list_penalties.append(
            penalty
        )
    
    print("list_penalties",list_penalties[0])
    

    return list_penalties

""" penalty_schema.Penalty(
                id = penalty.id,
                days_late = penalty.days_late,
                total_taxes = penalty.total_taxes,
                state = penalty.state,
                lending_id = penalty.lending_id.id,
                created_at = penalty.created_at,
            ) """
def delete_penalty(penalty_id: int):
    penalty = PenaltyModel.filter((PenaltyModel.id == penalty_id)).first()

    if not penalty:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Penalty not found"
        )

    penalty.delete_instance()