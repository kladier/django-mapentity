# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import migrations
import django.contrib.admin.models
import mapentity.models


class Migration(migrations.Migration):

    dependencies = [
        ('mapentity', '0001_initial'),
    ]

    operations = [
        migrations.RunSQL("""
                          CREATE TABLE public.mapentity_mushroomspot
                          (
                          id serial NOT NULL,
                          serialized character varying(200),
                          "number" integer DEFAULT 42,
                          size double precision DEFAULT 3.14159,
                          "boolean" boolean NOT NULL DEFAULT true,
                          name character varying(100) DEFAULT 'Empty'::character varying
                          );
                          """),
        migrations.RunSQL("""
                          CREATE TABLE public.mapentity_weatherstation
                          (
                              id serial NOT NULL,
                              geom geometry(Point,2154)
                          );
                          """),
        migrations.RunSQL("""
                          CREATE TABLE public.mapentity_dummymodel
                          (
                              id serial NOT NULL,
                              name character varying(128) DEFAULT ''::character varying,
                              geom geometry(Point,2154),
                              date_update date,
                              public boolean DEFAULT False
                          );
                          """),
        migrations.CreateModel(
            name='LogEntry',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=(mapentity.models.MapEntityMixin, 'admin.logentry'),
            managers=[
                ('objects', django.contrib.admin.models.LogEntryManager()),
            ],
        ),
    ]
