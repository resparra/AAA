from django.contrib import admin
from reports.models import Report,Polygon

admin.site.register(Report)
admin.site.register(Polygon)

class ReportInline(admin.TabularInline):
	model = Report
	extra = 3

class RerportAdmin(admin.ModelAdmin):
	fieldsets =(
		('', {
			'fields':('description','date', 'rep_type', 'status','status_comment',
			'latitude', 'longitude', 'count', 'email', 'photo_path'),
		}),

		('Flags', {
			'classes': ('grp-collapse grp-closed',),
			'fields' : ('flag_front', 'flag_sticky', 'flag_allow_comments', 'flag_comments_closed',),
		}),

		('Tags', {
            'classes': ('grp-collapse grp-open',),
            'fields' : ('tags',),
        }),
	)

class NavigationReportInline(admin.StackedInline):
	classes = ('grp-collapse grp-open',)
	inline_classes = ('grp-collapse grp-open',)
