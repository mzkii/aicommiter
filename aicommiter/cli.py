import click
from .init_branch import init_branch
from .commit import commit_changes
from .pr import create_pr
from .pr_preview import preview_pr

@click.group()
def cli():
    """AI Committer CLI"""
    pass

@cli.command()
def init():
    """Initialize branch name and create new branch"""
    init_branch()

@cli.command()
def commit():
    """Generate and commit with AI-generated message"""
    commit_changes()

@cli.command()
def pr():
    """Create pull request with a filled template"""
    create_pr()

@cli.command()
def preview():
    """Preview pull request content only"""
    preview_pr()
