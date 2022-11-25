from fastapi import HTTPException, status

from app.v1.schema import penalty_schema
from app.v1.models.penalty_model import Penalty as PenaltyModel


def add_(penalty: penalty_schema.Penalty):

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
    penalties = PenaltyModel.filter(PenaltyModel.id == PenaltyModel.id).order_by(PenaltyModel.created_at.desc())

    list_penalties = []
    for penalty in penalties:
        list_penalties.append(penalty_schema.Penalty(
                id = penalty.id,
                days_late = penalty.days_late,
                total_taxes = penalty.total_taxes,
                state = penalty.state,
                lending_id = penalty.lending_id,
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
        lending_id = penalty.lending_id,
        created_at = penalty.created_at,
    )

def update_state_penalty(state: str, penalty_id: int):
    penalty = PenaltyModel.filter((PenaltyModel.id == penalty_id)).first()

    if not penalty:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Penalty not found"
        )

    penalty.state = state
    penalty.save()

    return penalty_schema.Penalty(
        id = penalty.id,
        days_late = penalty.days_late,
        total_taxes = penalty.total_taxes,
        state = penalty.state,
        lending_id = penalty.lending_id,
        created_at = penalty.created_at,
    )


def delete_penalty(penalty_id: int):
    penalty = PenaltyModel.filter((PenaltyModel.id == penalty_id)).first()

    if not penalty:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Penalty not found"
        )

    penalty.delete_instance()