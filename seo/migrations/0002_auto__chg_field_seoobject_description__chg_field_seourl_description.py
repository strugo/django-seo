# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'SeoObject.description'
        db.alter_column('seo_seoobject', 'description', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'SeoURL.description'
        db.alter_column('seo_seourl', 'description', self.gf('django.db.models.fields.TextField')(null=True))

    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'SeoObject.description'
        raise RuntimeError("Cannot reverse this migration. 'SeoObject.description' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'SeoURL.description'
        raise RuntimeError("Cannot reverse this migration. 'SeoURL.description' and its values cannot be restored.")

    models = {
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'seo.seoobject': {
            'Meta': {'object_name': 'SeoObject'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.TextField', [], {}),
            'object_pk': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        'seo.seourl': {
            'Meta': {'object_name': 'SeoURL'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['seo']