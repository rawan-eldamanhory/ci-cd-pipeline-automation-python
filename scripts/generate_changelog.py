#!/usr/bin/env python3
"""
Changelog Generator.

Automatically generates a CHANGELOG.md file from git commit messages.

This script analyzes git commit history and categorizes commits into:
- Features (feat:)
- Bug Fixes (fix:)
- Documentation (docs:)
- Refactoring (refactor:)
- Tests (test:)
- Chores (chore:)
"""

import re
import subprocess
from collections import defaultdict
from datetime import datetime
from typing import Dict, List, Tuple


class ChangelogGenerator:
    """Generates changelog from git commits using conventional commits."""

    def __init__(self):
        self.commit_types = {
            'feat': 'Features',
            'fix': 'Bug Fixes',
            'docs': 'Documentation',
            'style': 'Styles',
            'refactor': 'Code Refactoring',
            'perf': 'Performance',
            'test': 'Tests',
            'build': 'Build System',
            'ci': 'CI/CD',
            'chore': 'Chores',
            'revert': 'Reverts',
        }

    def get_git_tags(self) -> List[str]:
        """
        Get list of git tags sorted by date.
        """
        try:
            result = subprocess.run(
                ['git', 'tag', '--sort=-creatordate'],
                capture_output=True,
                text=True,
                check=True
            )
            tags = result.stdout.strip().split('\n')
            return [tag for tag in tags if tag]
        except subprocess.CalledProcessError:
            return []

    def get_commits_between(
        self, from_ref: str = None, to_ref: str = 'HEAD'
    ) -> List[Dict]:
        """
        Get commits between two references.
        """
        try:
            if from_ref:
                ref_range = f'{from_ref}..{to_ref}'
            else:
                ref_range = to_ref

            result = subprocess.run(
                [
                    'git', 'log', ref_range,
                    '--pretty=format:%H|%s|%an|%ad',
                    '--date=short'
                ],
                capture_output=True,
                text=True,
                check=True
            )

            commits = []
            for line in result.stdout.strip().split('\n'):
                if not line:
                    continue

                parts = line.split('|')
                if len(parts) >= 4:
                    commit_hash, message, author, date = parts[:4]
                    commits.append({
                        'hash': commit_hash[:7],
                        'message': message,
                        'author': author,
                        'date': date
                    })

            return commits

        except subprocess.CalledProcessError:
            return []

    def categorize_commit(self, message: str) -> Tuple[str, str]:
        """
        Categorize commit based on conventional commit format.
        """
        pattern = r'^(\w+)(?:\(([^)]+)\))?: (.+)$'
        match = re.match(pattern, message)

        if match:
            commit_type = match.group(1).lower()
            scope = match.group(2)
            description = match.group(3)

            if commit_type in self.commit_types:
                if scope:
                    cleaned = f"**{scope}**: {description}"
                else:
                    cleaned = description
                return commit_type, cleaned

        return 'other', message

    def group_commits_by_type(
        self, commits: List[Dict]
    ) -> Dict[str, List[Dict]]:
        """
        Group commits by their type.
        """
        grouped = defaultdict(list)

        for commit in commits:
            commit_type, cleaned_message = self.categorize_commit(
                commit['message']
            )
            commit['cleaned_message'] = cleaned_message
            commit['type'] = commit_type
            grouped[commit_type].append(commit)

        return dict(grouped)

    def generate_version_section(
        self, version: str, date: str, commits: List[Dict]
    ) -> str:
        """
        Generate changelog section for a version.
        """
        lines = []
        lines.append(f"## [{version}] - {date}")
        lines.append("")

        grouped = self.group_commits_by_type(commits)

        for commit_type in self.commit_types.keys():
            if commit_type in grouped and grouped[commit_type]:
                section_title = self.commit_types[commit_type]
                lines.append(f"### {section_title}")
                lines.append("")

                for commit in grouped[commit_type]:
                    lines.append(
                        f"- {commit['cleaned_message']} "
                        f"([{commit['hash']}])"
                    )
                lines.append("")

        if 'other' in grouped and grouped['other']:
            lines.append("### Other Changes")
            lines.append("")
            for commit in grouped['other']:
                lines.append(
                    f"- {commit['cleaned_message']} ([{commit['hash']}])"
                )
            lines.append("")

        return '\n'.join(lines)

    def generate_changelog(self) -> str:
        """
        Generate complete changelog.
        """
        lines = []

        lines.append("# Changelog")
        lines.append("")
        lines.append(
            "All notable changes to this project will be "
            "documented in this file."
        )
        lines.append("")
        lines.append(
            "The format is based on "
            "[Keep a Changelog](https://keepachangelog.com/en/1.0.0/),"
        )
        lines.append(
            "and this project adheres to "
            "[Semantic Versioning](https://semver.org/spec/v2.0.0.html)."
        )
        lines.append("")

        tags = self.get_git_tags()

        if tags:
            for i, tag in enumerate(tags):
                next_tag = tags[i + 1] if i + 1 < len(tags) else None
                commits = self.get_commits_between(next_tag, tag)

                if commits:
                    try:
                        result = subprocess.run(
                            [
                                'git', 'log', '-1',
                                '--format=%ad', '--date=short', tag
                            ],
                            capture_output=True,
                            text=True,
                            check=True
                        )
                        tag_date = result.stdout.strip()
                    except subprocess.CalledProcessError:
                        tag_date = datetime.now().strftime('%Y-%m-%d')

                    lines.append(
                        self.generate_version_section(tag, tag_date, commits)
                    )

            unreleased = self.get_commits_between(tags[0], 'HEAD')
            if unreleased:
                lines.insert(7, self.generate_version_section(
                    'Unreleased',
                    datetime.now().strftime('%Y-%m-%d'),
                    unreleased
                ))
                lines.insert(8, "")
        else:
            all_commits = self.get_commits_between()
            if all_commits:
                lines.append(self.generate_version_section(
                    'Unreleased',
                    datetime.now().strftime('%Y-%m-%d'),
                    all_commits
                ))

        return '\n'.join(lines)

    def save_changelog(self, filename: str = 'CHANGELOG.md'):
        """
        Generate and save changelog to file.
        """
        changelog = self.generate_changelog()

        with open(filename, 'w') as f:
            f.write(changelog)

        print(f"Changelog generated: {filename}")
        print(f"Lines: {len(changelog.splitlines())}")


def main():
    print("="*60)
    print("  CHANGELOG GENERATOR")
    print("="*60)
    print()

    try:
        generator = ChangelogGenerator()
        generator.save_changelog()

        print()
        print("="*60)
        print("  Changelog generation complete!")
        print("="*60)

    except Exception as e:
        print(f"Error generating changelog: {str(e)}")
        return 1

    return 0


if __name__ == '__main__':
    exit(main())
