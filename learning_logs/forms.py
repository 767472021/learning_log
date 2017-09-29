#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2017/9/10 16:12
# @Author  : Rain
# @File    : forms.py
# @Software: PyCharm
from django import forms
from .models import Topic, Entry
class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}