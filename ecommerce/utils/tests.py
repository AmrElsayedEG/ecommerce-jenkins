from rest_framework.test import APITestCase
from django.urls import reverse
from mixer.backend.django import Mixer, GenFactory
from rest_framework import status

mixer = Mixer(factory=GenFactory)