# -*- coding: utf-8 -*-

from south.db import db
from django.db import models
from iBanners.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding model 'Banner'
        db.create_table('iBanners_banner', (
            ('id', orm['iBanners.Banner:id']),
            ('campaign', orm['iBanners.Banner:campaign']),
            ('banner_type', orm['iBanners.Banner:banner_type']),
            ('name', orm['iBanners.Banner:name']),
            ('foreign_url', orm['iBanners.Banner:foreign_url']),
            ('width', orm['iBanners.Banner:width']),
            ('height', orm['iBanners.Banner:height']),
            ('clicks', orm['iBanners.Banner:clicks']),
            ('shows', orm['iBanners.Banner:shows']),
            ('max_clicks', orm['iBanners.Banner:max_clicks']),
            ('max_shows', orm['iBanners.Banner:max_shows']),
            ('begin_date', orm['iBanners.Banner:begin_date']),
            ('end_date', orm['iBanners.Banner:end_date']),
            ('swf_file', orm['iBanners.Banner:swf_file']),
            ('img_file', orm['iBanners.Banner:img_file']),
            ('alt', orm['iBanners.Banner:alt']),
            ('comment', orm['iBanners.Banner:comment']),
            ('html_text', orm['iBanners.Banner:html_text']),
            ('var', orm['iBanners.Banner:var']),
        ))
        db.send_create_signal('iBanners', ['Banner'])
        
        # Adding model 'Zone'
        db.create_table('iBanners_zone', (
            ('id', orm['iBanners.Zone:id']),
            ('site', orm['iBanners.Zone:site']),
            ('name', orm['iBanners.Zone:name']),
            ('description', orm['iBanners.Zone:description']),
            ('price', orm['iBanners.Zone:price']),
            ('html_after_banner', orm['iBanners.Zone:html_after_banner']),
            ('html_pre_banner', orm['iBanners.Zone:html_pre_banner']),
        ))
        db.send_create_signal('iBanners', ['Zone'])
        
        # Adding model 'Campaign'
        db.create_table('iBanners_campaign', (
            ('id', orm['iBanners.Campaign:id']),
            ('client', orm['iBanners.Campaign:client']),
            ('name', orm['iBanners.Campaign:name']),
            ('begin_date', orm['iBanners.Campaign:begin_date']),
            ('end_date', orm['iBanners.Campaign:end_date']),
            ('priority', orm['iBanners.Campaign:priority']),
        ))
        db.send_create_signal('iBanners', ['Campaign'])
        
        # Adding model 'Client'
        db.create_table('iBanners_client', (
            ('id', orm['iBanners.Client:id']),
            ('name', orm['iBanners.Client:name']),
            ('contact', orm['iBanners.Client:contact']),
            ('email', orm['iBanners.Client:email']),
            ('one_banner_per_page', orm['iBanners.Client:one_banner_per_page']),
        ))
        db.send_create_signal('iBanners', ['Client'])
        
        # Adding ManyToManyField 'Banner.zones'
        db.create_table('iBanners_banner_zones', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('banner', models.ForeignKey(orm.Banner, null=False)),
            ('zone', models.ForeignKey(orm.Zone, null=False))
        ))
        
    
    
    def backwards(self, orm):
        
        # Deleting model 'Banner'
        db.delete_table('iBanners_banner')
        
        # Deleting model 'Zone'
        db.delete_table('iBanners_zone')
        
        # Deleting model 'Campaign'
        db.delete_table('iBanners_campaign')
        
        # Deleting model 'Client'
        db.delete_table('iBanners_client')
        
        # Dropping ManyToManyField 'Banner.zones'
        db.delete_table('iBanners_banner_zones')
        
    
    
    models = {
        'iBanners.banner': {
            'alt': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'banner_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'begin_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'campaign': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['iBanners.Campaign']"}),
            'clicks': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'blank': 'True'}),
            'comment': ('django.db.models.fields.TextField', [], {'default': "''", 'max_length': '255', 'blank': 'True'}),
            'end_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'foreign_url': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'height': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'html_text': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'img_file': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'max_clicks': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'blank': 'True'}),
            'max_shows': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'shows': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'blank': 'True'}),
            'swf_file': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'var': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'width': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'zones': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['iBanners.Zone']"})
        },
        'iBanners.campaign': {
            'begin_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'client': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['iBanners.Client']"}),
            'end_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'priority': ('django.db.models.fields.IntegerField', [], {})
        },
        'iBanners.client': {
            'contact': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'one_banner_per_page': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'})
        },
        'iBanners.zone': {
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'html_after_banner': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'blank': 'True'}),
            'html_pre_banner': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'price': ('django.db.models.fields.IntegerField', [], {}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sites.Site']"})
        },
        'sites.site': {
            'Meta': {'db_table': "'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }
    
    complete_apps = ['iBanners']
