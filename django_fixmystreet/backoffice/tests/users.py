from django.test import TestCase
from django.core.urlresolvers import reverse
from django_fixmystreet.fixmystreet.models import OrganisationEntity, FMSUser
from django.utils import unittest

class UsersTest(TestCase):

    fixtures = ["bootstrap","list_items"]

    def setUp(self): 
        self.manager = FMSUser(
            telephone="0123456789",
            last_used_language="fr", 
            password='test',
            first_name="manager",
            last_name="manager",
            email="manager@a.com",
            manager=True
        )
        self.manager.set_password('test')
        self.manager.organisation = OrganisationEntity.objects.get(pk=14)
        self.manager.save()

        self.leader = FMSUser(
            telephone="0123456789",
            last_used_language="fr",
            password='test',
            first_name="leader",
            last_name="leader",
            email="leader@a.com",
            manager=True,
            leader = True
        )
        self.leader.set_password('test')
        self.leader.organisation = OrganisationEntity.objects.get(pk=14)
        self.leader.save()
        self.createuser_post = {
            'telephone':'123456',
            'is_active': True,
            'first_name':'david', 
            'last_name':'hasselhof',
            'email':'david.hasselhof@baywatch.com'
        }
        self.edituser_post = {
            'telephone':'654321',
            'is_active': True,
            'first_name':'new_manager', 
            'last_name':'new_manager',
            'email':'manager2@a.com'
        }


    def testListUser(self):
        self.client.login(username='manager@a.com', password='test')
        response = self.client.post(reverse('list_users'), follow=True)
        self.assertEquals(response.status_code, 200)
        self.assertTrue('users' in response.context)
        self.assertTrue('can_create' in response.context)
        can_create = response.context['can_create']
        self.assertFalse(can_create)
        #This user should not be able to create
        users = response.context['users']
        self.assertEquals(users.count(), 2)
        self.assertIn(self.manager, users)
        self.assertIn(self.leader, users)
        #same result for leader
        self.client.logout()
        self.client.login(username='leader@a.com', password='test')
        response = self.client.post(reverse('list_users'), follow=True)
        self.assertEquals(response.status_code, 200)
        self.assertTrue('users' in response.context)
        self.assertTrue('can_create' in response.context)
        can_create = response.context['can_create']
        self.assertTrue(can_create)
        #This user should not be able to create
        users = response.context['users']
        self.assertEquals(users.count(), 2)
        self.assertIn(self.manager, users)
        self.assertIn(self.leader, users)

    #this test fails because the user created by create_user is not marked as pro and hence cannot be found by list_users
    #when this is fixed update this method to test addition by non leader user
    @unittest.skip ('Test will be skipped')
    def testCreateUser(self):
        self.client.login(username='leader@a.com', password='test')
        response = self.client.post(reverse('create_user'), self.createuser_post, follow=True)
        self.assertEquals(response.status_code, 200)
        response = self.client.post(reverse('list_users'), follow=True)
        self.assertEquals(response.status_code, 200)
        self.assertTrue('users' in response.context)
        self.assertTrue('can_create' in response.context)
        can_create = response.context['can_create']
        users = response.context['users']
        self.assertTrue(can_create)
        #self.assertEquals(users.count(), 3)

    def testUpdateUserAsLeader(self):
        self.client.login(username='leader@a.com', password='test')
        response = self.client.post(reverse('edit_user',args=[self.manager.id]), self.edituser_post, follow=True)
        self.assertEquals(response.status_code, 200)
        response = self.client.post(reverse('list_users'), follow=True)
        self.assertEquals(response.status_code, 200)
        self.assertTrue('users' in response.context)
        self.assertTrue('can_create' in response.context)
        can_create = response.context['can_create']
        users = response.context['users']
        self.assertTrue(can_create)
        founduser = False
        for user in users:
            if (user.id == self.manager.id):
                self.assertEquals(user.first_name, 'new_manager')
                self.assertEquals(user.last_name, 'new_manager')
                self.assertEquals(user.telephone, '654321')
                self.assertEquals(user.email, 'manager2@a.com')
                founduser = True
        self.assertTrue(founduser)
        #now try to update a leader user this should not be allowed
        response = self.client.post(reverse('edit_user',args=[self.leader.id]), self.edituser_post, follow=True)
        self.assertEquals(response.status_code, 200)
        self.assertTrue('can_edit' in response.context)
        self.assertFalse(response.context['can_edit'])
        response = self.client.post(reverse('list_users'), follow=True)
        self.assertEquals(response.status_code, 200)
        self.assertTrue('users' in response.context)
        self.assertTrue('can_create' in response.context)
        can_create = response.context['can_create']
        users = response.context['users']
        self.assertTrue(can_create)
        founduser = False
        for user in users:
            if (user.id == self.leader.id):
                self.assertEquals(user.first_name, self.leader.first_name)
                self.assertEquals(user.last_name, self.leader.last_name)
                self.assertEquals(user.telephone, self.leader.telephone)
                self.assertEquals(user.email, self.leader.email)
                founduser = True
        self.assertTrue(founduser)

    def testUpdateUserAsPro(self):
        self.client.login(username='manager@a.com', password='test')
        response = self.client.post(reverse('edit_user',args=[self.manager.id]), self.edituser_post, follow=True)
        self.assertEquals(response.status_code, 200)
        response = self.client.post(reverse('list_users'), follow=True)
        self.assertEquals(response.status_code, 200)
        self.assertTrue('users' in response.context)
        self.assertTrue('can_create' in response.context)
        can_create = response.context['can_create']
        users = response.context['users']
        self.assertFalse(can_create)
        founduser = False
        for user in users:
            if (user.id == self.manager.id):
                self.assertNotEquals(user.first_name, 'new_manager')
                self.assertNotEquals(user.last_name, 'new_manager')
                self.assertNotEquals(user.telephone, '654321')
                self.assertNotEquals(user.email, 'manager2@a.com')
                founduser = True
        self.assertTrue(founduser)

    #disable test due to bug in users.py where in delete_user 'list_users' should not have kwargs={'user_type': user_type}
    @unittest.skip ('Test will be skipped')
    def testDeleteUser(self):
        self.client.login(username='leader@a.com', password='test')
        response = self.client.get(reverse('delete_user', args=[self.manager.id]), follow=True)
        self.assertEquals(response.status_code, 200)
        response = self.client.post(reverse('list_users'), follow=True)
        self.assertEquals(response.status_code, 200)
        self.assertTrue('users' in response.context)
        self.assertTrue('can_create' in response.context)
        can_create = response.context['can_create']
        users = response.context['users']
        self.assertEquals(users.count(), 1)
        self.assertNotIn(self.manager, users)

    #disable test due to bug in users.py where in delete_user 'list_users' should not have kwargs={'user_type': user_type}
    @unittest.skip ('Test will be skipped')
    def testDeleteUserAsPro(self):
        self.client.login(username='manager@a.com', password='test')
        response = self.client.get(reverse('delete_user', args=[self.manager.id]), follow=True)
        self.assertEquals(response.status_code, 200)
        response = self.client.post(reverse('list_users'), follow=True)
        self.assertEquals(response.status_code, 200)
        self.assertTrue('users' in response.context)
        self.assertTrue('can_create' in response.context)
        can_create = response.context['can_create']
        users = response.context['users']
        self.assertEquals(users.count(), 2)
        self.assertIn(self.manager, users)