# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.template import loader, Context
from django.http import HttpResponse
from django.shortcuts import render_to_response
from blog.models import Author,Books

def result(req):
	booklist = []
	authorname = req.GET['authorname']
	books =  Books.objects.all()
	author = Author.objects.get(name = authorname)
	for book in books:
		if book.authorid == author.authorid:
			booklist.append(book)
	return render_to_response('result.html', {'booklist':booklist})

def backresult(req):
	authorid = req.GET['authorid']
	books =  Books.objects.all()
	booklist = []
	author = Author.objects.get(authorid = authorid)
	for book in books:
		if book.authorid == author.authorid:
			booklist.append(book)
	return render_to_response('result.html', {'booklist':booklist})

def search(req):
	return render_to_response('home.html')
def adda(req):
	id_list=[]
	authors =  Author.objects.all()
	for author in authors:
		id_list.append(author.name)
		id_list.append(author.authorid)
	return render_to_response('addauthor.html',{'idlist':id_list})
def addb(req):
	id_list=[]
	authors =  Author.objects.all()
	for author in authors:
		id_list.append(author.authorid)
	return render_to_response('addbook.html',{'idlist':id_list})
def delete(req):
	booktitle = req.GET['booktitle']
	books =  Books.objects.all()
	for book in books:
		if book.title == booktitle:
			 authorid	= book.authorid
	Books.objects.get( title = booktitle).delete()
	return render_to_response('delete.html',{'authorid':authorid})

	
	
def message(req):
	bookisbn = req.GET['bookisbn']
	books =  Books.objects.all()
	for book in books:
		if book.isbn == bookisbn:
			typicalbook = book
	return render_to_response('message.html',{'books':typicalbook})
def addauthor(req):
	addname = req.GET['authorname']
	addid = req.GET['authorid']
	addage = req.GET['authorage']
	addcountry = req.GET['authorcountry']
	Author.objects.create(name = addname,authorid = addid,age = addage,country = addcountry)
	return render_to_response('addresult_a.html')
def addbook(req):
	addtitle = req.GET['booktitle']
	addid = req.GET['authorid']
	addisbn = req.GET['bookisbn']
	addpublisher = req.GET['bookpublisher']
	adddate = req.GET['bookdate']
	addprice = req.GET['bookprice']
	Books.objects.create( title= addtitle,authorid = addid, isbn = addisbn,publisher = addpublisher,publication_date = adddate ,price = addprice)
	return render_to_response('addresult_a.html')