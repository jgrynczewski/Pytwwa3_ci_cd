from django.test import TestCase
from django.test import Client

from .models import Message

# Create your tests here.

class MessageTestCase(TestCase):
    def setUp(self):
        m1 = Message.objects.create(
            name = "Jan Kołodziej",
            email = "jan@kołodziej.com",
            priority = 4,
            category = "question",
            subject = "Kto to?",
            body = "Puste",
        )
        m2 = Message.objects.create(
            name = "Ewa Kowal",
            email = "ewa@kowal.com",
            priority = 9,
            category = "other",
            subject = "Co to?",
            body = "Bla bla",
        )
        m3 = Message.objects.create(
            name = "Adam Bartnik",
            email = "adam@bartnik.com",
            priority = 43,
            category = "question",
            subject = "Gdzie?",
            body = "Lorem ipsum lorem",
        )

    ### Testowanie modelu znajdującego się na serwerze

    def test_create_object(self):
        length = len(Message.objects.all())
        self.assertEqual(length, 3)

    def test_valid_message(self):
        m = Message.objects.get(id=1)
        self.assertTrue(m.is_valid_message())

    def test_invalid_message(self):
        m = Message.objects.filter(name="Adam Bartnik").first()
        self.assertFalse(m.is_valid_message())

    def test_increase_priority(self):
        m = Message.objects.get(id=2)
        p = m.priority
        m.increase_priority()
        self.assertEqual(p+1, m.priority)

    def test_set_priority(self):
        m = Message.objects.get(id=1)
        m.set_priority(7)
        self.assertEqual(m.priority, 7)

    ### Testowanie odpowiedzi serwera

    def test_messages_response(self):
        c = Client()

        response = c.get("/crud/message-list")
        self.assertEqual(response.status_code, 200)

        context = response.context['object_list']
        self.assertEqual(len(context), 3)

    def test_messages_invalid_response(self):
        c = Client()
        response = c.get("/crud/message-list/5")
        self.assertEqual(response.status_code, 404)

    def test_messages_detail_response(self):
        c = Client()
        response = c.get("/crud/message-detail/2")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['object'].name, "Ewa Kowal")

    def test_message_form(self):
        c = Client()
        response = c.post('/crud/message-create', {
            'name': "Katarzyna Bartnik",
            "email": "katarzyna@bartnik.com",
            'priority': 6,
            'category': "question",
            'subject': "Pytanie",
            'body': "Treść pytania",
        })
        self.assertEqual(response.status_code, 302)
        m = Message.objects.all()
        self.assertEqual(m.count(), 4)