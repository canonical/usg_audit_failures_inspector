"""Console script for usg_audit_failures_inspector."""
import sys
import click
from usg_audit_failures_inspector import process_audit_results

@click.command()
@click.option('--xml-audit-result', 'xml_audit_results',
              type=click.File(mode='r'),
              help='XML file from the `oscap xccdf eval` command. '
                   'Two files are required.',
              multiple=True, required=False, default=None)
def main(args=None, xml_audit_results=[]):
    """Console script for usg_audit_failures_inspector."""
    if len(xml_audit_results) != 2:
        raise(click.UsageError("Two XML files are required."))
    else:
        audit_results_diff = process_audit_results(xml_audit_results)
        # click.echo(audit_results_diff)

if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
