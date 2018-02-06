from django.contrib import admin

from apps.commits.models import Commit


class CommitAdmin(admin.ModelAdmin):
    list_display = [
        'git_hash', 'text', 'score', 'score_funny', 'score_not_funny'
    ]
    search_fields = ['text', 'git_hash']


admin.site.register(Commit, CommitAdmin)
