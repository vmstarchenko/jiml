import textwrap
import pathlib
import jiml


DATA_DIR = pathlib.Path(__file__).absolute().parent / 'data'


def test_load_template():
    t = jiml.load_template(textwrap.dedent(
        '''
        # options
        input_schema:
            properties:
                value: { type: string }
        ---
        key: {{ value }}
        '''
    ))
    f = jiml.testlib.TestFile(t, DATA_DIR / 'simple_template.test.yaml')
    f.run()
