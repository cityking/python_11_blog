# coding:utf-8
from django import template
register = template.Library()
def upper(key):
	return ['一','二','三','四','五','六','七','八','九','十','十一','十二',][int(key)-1]
register.filter('upper', upper)
