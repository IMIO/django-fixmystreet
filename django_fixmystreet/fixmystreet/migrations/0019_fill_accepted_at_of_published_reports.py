# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models

from django_fixmystreet.fixmystreet.models import Report, ReportEventLog

class Migration(DataMigration):

    def forwards(self, orm):
        "Write your forwards methods here."
        # Note: Remember to use orm['appname.ModelName'] rather than "from appname.models..."
        for report in orm.Report.objects.all():
            if not report.accepted_at and report.status != Report.CREATED and report.status != Report.REFUSED:
                # Find date for valid status in event_log and save as accepted_at
                event_logs = orm.ReportEventLog.objects.filter(report=report, event_type=ReportEventLog.VALID).order_by('event_at')
                if event_logs:
                    event_log = event_logs[0]
                    report.accepted_at = event_log.event_at
                    report.save()

    def backwards(self, orm):
        "Write your backwards methods here."
        raise RuntimeError("Cannot reverse this migration.")

    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '75'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'fixmystreet.faqentry': {
            'Meta': {'ordering': "['order']", 'object_name': 'FaqEntry'},
            'a_fr': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'a_nl': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'q_fr': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'q_nl': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        },
        u'fixmystreet.fmsuser': {
            'Meta': {'object_name': 'FMSUser', '_ormbases': [u'auth.User']},
            'agent': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'applicant': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'type'", 'blank': 'True', 'to': u"orm['fixmystreet.ReportCategory']"}),
            'contractor': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'fmsuser_created'", 'null': 'True', 'to': u"orm['fixmystreet.FMSUser']"}),
            'last_used_language': ('django.db.models.fields.CharField', [], {'default': "'FR'", 'max_length': '10', 'null': 'True'}),
            'leader': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'logical_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'manager': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'fmsuser_modified'", 'null': 'True', 'to': u"orm['fixmystreet.FMSUser']"}),
            'organisation': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'team'", 'null': 'True', 'to': u"orm['fixmystreet.OrganisationEntity']"}),
            'quality': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'telephone': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True'}),
            u'user_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True', 'primary_key': 'True'}),
            'work_for': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'workers'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['fixmystreet.OrganisationEntity']"})
        },
        u'fixmystreet.historicalfmsuser': {
            'Meta': {'ordering': "('-history_date', '-history_id')", 'object_name': 'HistoricalFMSUser'},
            'agent': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'applicant': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'contractor': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'created_by_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'db_index': 'True', 'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'history_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'history_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'history_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'history_user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True'}),
            u'id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True', 'blank': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'last_used_language': ('django.db.models.fields.CharField', [], {'default': "'FR'", 'max_length': '10', 'null': 'True'}),
            'leader': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'logical_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'manager': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'modified_by_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'organisation_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'quality': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'telephone': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True'}),
            u'user_ptr_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '75', 'db_index': 'True'})
        },
        u'fixmystreet.historicalorganisationentity': {
            'Meta': {'ordering': "('-history_date', '-history_id')", 'object_name': 'HistoricalOrganisationEntity'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'applicant': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'commune': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'created_by_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'dependency_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'feature_id': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'history_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'history_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'history_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'history_user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True'}),
            u'id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'modified_by_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'name_fr': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name_nl': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'region': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'slug_fr': ('django.db.models.fields.SlugField', [], {'max_length': '100'}),
            'slug_nl': ('django.db.models.fields.SlugField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'subcontractor': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'fixmystreet.historicalreport': {
            'Meta': {'ordering': "('-history_date', '-history_id')", 'object_name': 'HistoricalReport'},
            'accepted_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'address_fr': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'address_nl': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'address_number': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'address_number_as_int': ('django.db.models.fields.IntegerField', [], {'max_length': '255'}),
            'address_regional': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'category_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'citizen_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'close_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'contractor_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'created_by_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'date_planned': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'fixed_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'gravity': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'hash_code': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'history_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'history_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'history_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'history_user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True'}),
            u'id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True', 'blank': 'True'}),
            'mark_as_done_motivation': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'mark_as_done_user_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'modified_by_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'photo': ('django.db.models.fields.TextField', [], {'max_length': '100', 'blank': 'True'}),
            'planned': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'point': ('django.contrib.gis.db.models.fields.PointField', [], {'srid': '31370', 'null': 'True', 'blank': 'True'}),
            'postalcode': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'private': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'probability': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'quality': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'refusal_motivation': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'responsible_entity_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'responsible_manager_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'responsible_manager_validated': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'secondary_category_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'terms_of_use_validated': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'valid': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'fixmystreet.listitem': {
            'Meta': {'object_name': 'ListItem'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label_fr': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'label_nl': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'model_class': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'model_field': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'fixmystreet.mailnotificationtemplate': {
            'Meta': {'object_name': 'MailNotificationTemplate'},
            'content_fr': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'content_nl': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'title_fr': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'title_nl': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        u'fixmystreet.organisationentity': {
            'Meta': {'object_name': 'OrganisationEntity'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'applicant': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'commune': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'organisationentity_created'", 'null': 'True', 'to': u"orm['fixmystreet.FMSUser']"}),
            'dependency': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'associates'", 'null': 'True', 'to': u"orm['fixmystreet.OrganisationEntity']"}),
            'feature_id': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'organisationentity_modified'", 'null': 'True', 'to': u"orm['fixmystreet.FMSUser']"}),
            'name_fr': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name_nl': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'region': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'slug_fr': ('django.db.models.fields.SlugField', [], {'max_length': '100'}),
            'slug_nl': ('django.db.models.fields.SlugField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'subcontractor': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'fixmystreet.report': {
            'Meta': {'object_name': 'Report'},
            'accepted_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'address_fr': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'address_nl': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'address_number': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'address_number_as_int': ('django.db.models.fields.IntegerField', [], {'max_length': '255'}),
            'address_regional': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['fixmystreet.ReportMainCategoryClass']", 'null': 'True', 'blank': 'True'}),
            'citizen': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'citizen_reports'", 'null': 'True', 'to': u"orm['fixmystreet.FMSUser']"}),
            'close_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'contractor': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'assigned_reports'", 'null': 'True', 'to': u"orm['fixmystreet.OrganisationEntity']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'report_created'", 'null': 'True', 'to': u"orm['fixmystreet.FMSUser']"}),
            'date_planned': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'fixed_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'gravity': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'hash_code': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mark_as_done_motivation': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'mark_as_done_user': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'reports_solved'", 'null': 'True', 'to': u"orm['fixmystreet.FMSUser']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'report_modified'", 'null': 'True', 'to': u"orm['fixmystreet.FMSUser']"}),
            'photo': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'planned': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'point': ('django.contrib.gis.db.models.fields.PointField', [], {'srid': '31370', 'null': 'True', 'blank': 'True'}),
            'postalcode': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'previous_managers': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'previous_reports'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['fixmystreet.FMSUser']"}),
            'private': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'probability': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'quality': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'refusal_motivation': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'responsible_entity': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'reports_in_charge'", 'null': 'True', 'to': u"orm['fixmystreet.OrganisationEntity']"}),
            'responsible_manager': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'reports_in_charge'", 'null': 'True', 'to': u"orm['fixmystreet.FMSUser']"}),
            'responsible_manager_validated': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'secondary_category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['fixmystreet.ReportCategory']", 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'terms_of_use_validated': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'valid': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'fixmystreet.reportattachment': {
            'Meta': {'object_name': 'ReportAttachment'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reportattachment_created'", 'null': 'True', 'to': u"orm['fixmystreet.FMSUser']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logical_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reportattachment_modified'", 'null': 'True', 'to': u"orm['fixmystreet.FMSUser']"}),
            'report': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'attachments'", 'to': u"orm['fixmystreet.Report']"}),
            'security_level': ('django.db.models.fields.IntegerField', [], {'default': '2'})
        },
        u'fixmystreet.reportcategory': {
            'Meta': {'object_name': 'ReportCategory'},
            'category_class': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'categories'", 'to': u"orm['fixmystreet.ReportMainCategoryClass']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reportcategory_created'", 'null': 'True', 'to': u"orm['fixmystreet.FMSUser']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reportcategory_modified'", 'null': 'True', 'to': u"orm['fixmystreet.FMSUser']"}),
            'name_fr': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name_nl': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'public': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'secondary_category_class': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'categories'", 'to': u"orm['fixmystreet.ReportSecondaryCategoryClass']"}),
            'slug_fr': ('django.db.models.fields.SlugField', [], {'max_length': '100'}),
            'slug_nl': ('django.db.models.fields.SlugField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        u'fixmystreet.reportcategoryhint': {
            'Meta': {'object_name': 'ReportCategoryHint'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label_fr': ('django.db.models.fields.TextField', [], {}),
            'label_nl': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        u'fixmystreet.reportcomment': {
            'Meta': {'object_name': 'ReportComment', '_ormbases': [u'fixmystreet.ReportAttachment']},
            u'reportattachment_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['fixmystreet.ReportAttachment']", 'unique': 'True', 'primary_key': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {})
        },
        u'fixmystreet.reporteventlog': {
            'Meta': {'ordering': "['event_at']", 'object_name': 'ReportEventLog'},
            'event_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'event_type': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'organisation': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'activities'", 'to': u"orm['fixmystreet.OrganisationEntity']"}),
            'related_content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']", 'null': 'True'}),
            'related_new_id': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'related_old_id': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'report': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'activities'", 'to': u"orm['fixmystreet.Report']"}),
            'status_new': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'status_old': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'activities'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'value_old': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'})
        },
        u'fixmystreet.reportfile': {
            'Meta': {'object_name': 'ReportFile', '_ormbases': [u'fixmystreet.ReportAttachment']},
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'file_creation_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'file_type': ('django.db.models.fields.IntegerField', [], {}),
            'image': ('django_fixmystreet.fixmystreet.utils.FixStdImageField', [], {'max_length': '100', 'name': "'image'", 'blank': 'True'}),
            u'reportattachment_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['fixmystreet.ReportAttachment']", 'unique': 'True', 'primary_key': 'True'}),
            'title': ('django.db.models.fields.TextField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'})
        },
        u'fixmystreet.reportmaincategoryclass': {
            'Meta': {'object_name': 'ReportMainCategoryClass'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reportmaincategoryclass_created'", 'null': 'True', 'to': u"orm['fixmystreet.FMSUser']"}),
            'hint': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['fixmystreet.ReportCategoryHint']", 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reportmaincategoryclass_modified'", 'null': 'True', 'to': u"orm['fixmystreet.FMSUser']"}),
            'name_fr': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name_nl': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'slug_fr': ('django.db.models.fields.SlugField', [], {'max_length': '100'}),
            'slug_nl': ('django.db.models.fields.SlugField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        u'fixmystreet.reportnotification': {
            'Meta': {'object_name': 'ReportNotification'},
            'content_template': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'error_msg': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'recipient': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'notifications'", 'to': u"orm['fixmystreet.FMSUser']"}),
            'related_content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            'related_object_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'reply_to': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'sent_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'success': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'fixmystreet.reportsecondarycategoryclass': {
            'Meta': {'object_name': 'ReportSecondaryCategoryClass'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reportsecondarycategoryclass_created'", 'null': 'True', 'to': u"orm['fixmystreet.FMSUser']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'modified_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reportsecondarycategoryclass_modified'", 'null': 'True', 'to': u"orm['fixmystreet.FMSUser']"}),
            'name_fr': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name_nl': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'slug_fr': ('django.db.models.fields.SlugField', [], {'max_length': '100'}),
            'slug_nl': ('django.db.models.fields.SlugField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        u'fixmystreet.reportsubscription': {
            'Meta': {'unique_together': "(('report', 'subscriber'),)", 'object_name': 'ReportSubscription'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'report': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'subscriptions'", 'to': u"orm['fixmystreet.Report']"}),
            'subscriber': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['fixmystreet.FMSUser']"})
        },
        u'fixmystreet.streetsurface': {
            'Meta': {'object_name': 'StreetSurface'},
            'administrator': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'geom': ('django.contrib.gis.db.models.fields.GeometryField', [], {'srid': '31370'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pw_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'ssft': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'sslv': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'urbis_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'version_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'fixmystreet.zipcode': {
            'Meta': {'object_name': 'ZipCode'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'commune': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['fixmystreet.OrganisationEntity']"}),
            'hide': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name_fr': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name_nl': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['fixmystreet']
    symmetrical = True
