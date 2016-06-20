# -*- coding: utf-8 -*-
import random

from models import Epithet, Person


def db_fill_epithets():
    epithets = [u'милашка', u'солнцеликий', u'живорождённый', u'умелый', u'неопалимый', u'дезоксирибонуклеиновый',
                u'дерзкий', u'непьющий', u'быстрый', u'преподобный', u'молоденький', u'свежий', u'сухой', u'мокрый',
                u'унылый',  u'безотказный',  u'неотразимый',  u'модный ',  u'карколомный',  u'холостой',
                u'обаятельный',  u'строгий',  u'лукавый',  u'обескураженный' ]
    for epithet in epithets:
        Epithet(epithet=epithet).save()


def get_epithet(name):

    person = Person.objects(name=name).first()

    if person:
        return person.epithet
    else:
        epithets = Epithet.objects().all().values_list('epithet')
        num_of_epithets = Person.objects().count()

        choosen_epithet = epithets[random.randint(0, num_of_epithets)]

        Person(name=name, epithet=choosen_epithet).save()

        return choosen_epithet


def form_greeting(name):
    epithet = get_epithet(name)

    if type(name) == unicode:
        greet_phrase = u"Рад тебя видеть снова,  " + epithet + u' ' + name
    else:
        greet_phrase = u"Рад тебя видеть снова,  " + epithet + u' ' + name.encode("utf-8")
    return greet_phrase