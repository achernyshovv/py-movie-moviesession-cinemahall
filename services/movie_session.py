from datetime import datetime

from db.models import MovieSession


def create_movie_session(
        movie_show_time: datetime,
        movie_id: int,
        cinema_hall_id: int
) -> MovieSession:
    return MovieSession.objects.create(
        show_time=movie_show_time,
        movie_id=movie_id,
        cinema_hall_id=cinema_hall_id
    )


def get_movies_sessions(
        session_date: datetime = None
) -> MovieSession:
    sessions = MovieSession.objects.all()
    if session_date:
        sessions = sessions.filter(show_time__date=session_date)
    return sessions


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
        session_id: int,
        movie_id: int = None,
        cinema_hall_id: int = None,
        show_time: datetime = None
) -> MovieSession:
    session = get_movie_session_by_id(session_id)

    if movie_id:
        session.movie_id = movie_id

    if cinema_hall_id:
        session.cinema_hall_id = cinema_hall_id

    if show_time:
        session.show_time = show_time

    session.save()
    return session


def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.get(id=session_id).delete()