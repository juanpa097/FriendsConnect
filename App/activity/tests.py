from django.urls import reverse
from django.utils.timezone import make_aware
from rest_framework import status
from rest_framework.test import APITestCase
from .model import Activity, ActivityUser
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from datetime import datetime
import datetime as date
from django.utils import timezone


class ActivityTests(APITestCase):
    def setUp(self):
        self.username = "john"
        self.email = "john@snow.com"
        self.password = "you_know_nothing"
        self.user = User.objects.create_user(self.username, self.email,
                                             self.password)
        self.token = Token.objects.create(user=self.user)
        self.api_authentication()

    def test_create_Activity(self):
        """
        Ensure we can create a new account object.
        """
        url = reverse('activity')
        data = self._get_default_activity()
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Activity.objects.count(), 1)

    def test_get_Activities(self):
        """
        Get more than one item if get all activities
        """
        url = reverse('activity')
        data = self._get_default_activity()
        activity = Activity.objects.create(**data)
        ActivityUser.objects.create(
            user=self.user,
            activity=activity,
            rol=0
        )
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)
        self.assertEqual(len(response.data), 1)

    def test_query_activities(self):
        url = reverse('activity')
        data = self._get_default_activity()
        activity = Activity.objects.create(**data)
        ActivityUser.objects.create(
            user=self.user,
            activity=activity,
            rol=0
        )
        username = "john2"
        email = "john@snow2.com"
        password = "you_know_nothing"
        user = User.objects.create_user(username, email,
                                        password)
        ActivityUser.objects.create(
            user=user,
            activity=activity,
            rol=1
        )
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)
        self.assertEqual(len(response.data), 1)
        data_response = response.data[0]
        self.assertEqual(data_response['name'], activity.name)
        self.assertEqual(data_response['id'], activity.id)
        self.assertEqual(data_response['location'], activity.location)
        self.assertEqual(data_response['max_participants'],
                         activity.max_participants)
        self.assertEqual(data_response['image'], activity.image)
        self.assertEqual(data_response['author'], self.username)
        self.assertEqual(data_response['participants'], 2)
        self.assertEqual(data_response['comments'], 0)
        self.assertEqual(data_response['is_current_user_subscribed'], True)

    def test_create_Activity_date_less_now(self):
        """
                Ensure we can create a new account object.
                """
        url = reverse('activity')
        data = self._get_default_activity(
            begin_date='2010-09-04 06:00Z',
            end_date='2010-09-05 06:00Z',
        )
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Activity.objects.count(), 0)

    def test_create_Activity_max_participant_negative(self):
        """
        Ensure we can create a new account object.
        """
        url = reverse('activity')
        data = self._get_default_activity(max_participants=-1)
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Activity.objects.count(), 0)

    def test_get_activity(self):
        data = self._get_default_activity()
        activity = Activity.objects.create(**data)
        url = reverse('activity_pk', args=(activity.id,))
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)
        self.assertEqual(response.data['name'], "testAc")

    def test_put_activity(self):
        data = self._get_default_activity()
        activity = Activity.objects.create(**data)
        ActivityUser.objects.create(
            user=self.user,
            activity=activity,
            rol=0
        )
        url = reverse('activity_pk', args=(activity.id,))
        data['name'] = "test2"
        data['user_activity_id'] = self.user.id
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)
        self.assertEqual(response.data['name'], "test2")

    def test_delete_activity(self):
        data = self._get_default_activity()
        activity = Activity.objects.create(**data)
        ActivityUser.objects.create(
            user=self.user,
            activity=activity,
            rol=0
        )
        url = reverse('activity_pk', args=(activity.id,))
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Activity.objects.count(), 0)

    def test_begin_after_end_activity(self):
        time = datetime.now(tz=timezone.utc)
        time += date.timedelta(days=10)
        begin_date = time.strftime("%Y-%m-%d %H:%M:%S") + 'Z'
        end_date = time.strftime("%Y-%m-%d %H:%M:%S") + 'Z'
        data = self._get_default_activity(
            begin_date=begin_date,
            end_date=end_date
        )
        url = reverse('activity')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Activity.objects.count(), 0)

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_get_activity_by_username(self):
        data = self._get_default_activity()
        activity = Activity.objects.create(**data)
        activity2 = Activity.objects.create(**data)
        ActivityUser.objects.create(
            user=self.user,
            activity=activity,
            rol=0
        )
        ActivityUser.objects.create(
            user=self.user,
            activity=activity2,
            rol=1
        )
        url = reverse('activities_by_username', args=(self.username,))
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)
        self.assertEqual(len(response.data), 1)

    def test_get_activity_by_username_own(self):
        data = self._get_default_activity()
        activity = Activity.objects.create(**data)
        activity2 = Activity.objects.create(**data)
        ActivityUser.objects.create(
            user=self.user,
            activity=activity,
            rol=0
        )
        ActivityUser.objects.create(
            user=self.user,
            activity=activity2,
            rol=1
        )
        url = reverse('activities_by_username_own', args=(self.username,))
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)
        self.assertEqual(len(response.data), 1)

    @staticmethod
    def _get_default_activity(
            name="testAc",
            description="Des...",
            location="111",
            begin_date="",
            end_date="",
            max_participants=3,
            visibility="True"
    ):
        time = datetime.now(tz=timezone.utc)
        time += date.timedelta(days=10)
        if not begin_date:
            begin_date = time.strftime("%Y-%m-%d %H:%M:%S") + 'Z'
        if not end_date:
            end_date = \
                (time + date.timedelta(days=1)).strftime(
                    "%Y-%m-%d %H:%M:%S") + 'Z'

        data = {
            "name": name,
            "description": description,
            "location": location,
            "begin_date": begin_date,
            "end_date": end_date,
            "max_participants": max_participants,
            "visibility": visibility,
        }
        return data
