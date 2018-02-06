import os.path

from django.core.management import BaseCommand

from apps.commits.models import Commit


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str)

    def handle(self, *args, **options):
        file_path = options['file_path']
        print(file_path)
        file_path = os.path.expanduser(file_path)
        fd = open(file_path)

        for line in fd:
            line = line.strip()
            line_split = line.split(' ', 1)
            if len(line_split) == 1:
                continue
            git_hash, text = line_split
            try:
                Commit.objects.get_or_create(
                    git_hash=git_hash,
                    text=text
                )
            except ValueError:
                continue
