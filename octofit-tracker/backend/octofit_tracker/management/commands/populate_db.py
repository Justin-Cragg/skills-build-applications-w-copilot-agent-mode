from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Users
        ironman = User.objects.create(email='ironman@marvel.com', name='Iron Man', team='Marvel', is_superhero=True)
        batman = User.objects.create(email='batman@dc.com', name='Batman', team='DC', is_superhero=True)
        wonderwoman = User.objects.create(email='wonderwoman@dc.com', name='Wonder Woman', team='DC', is_superhero=True)
        spiderman = User.objects.create(email='spiderman@marvel.com', name='Spider-Man', team='Marvel', is_superhero=True)

        # Activities
        Activity.objects.create(user='Iron Man', activity_type='Run', duration=30, date='2025-09-01')
        Activity.objects.create(user='Batman', activity_type='Swim', duration=45, date='2025-09-02')
        Activity.objects.create(user='Wonder Woman', activity_type='Bike', duration=60, date='2025-09-03')
        Activity.objects.create(user='Spider-Man', activity_type='Climb', duration=25, date='2025-09-04')

        # Leaderboard
        Leaderboard.objects.create(team='Marvel', points=120)
        Leaderboard.objects.create(team='DC', points=110)

        # Workouts
        Workout.objects.create(name='Pushups', description='Do 20 pushups', difficulty='Easy')
        Workout.objects.create(name='Sprints', description='Run 5 sprints', difficulty='Medium')
        Workout.objects.create(name='Deadlift', description='Deadlift 100kg', difficulty='Hard')

        self.stdout.write(self.style.SUCCESS('Database populated successfully!'))
