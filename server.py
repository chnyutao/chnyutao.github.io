# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "flask",
# ]
# ///

import os
import subprocess
from tempfile import gettempdir

from flask import Flask, abort, request, send_file

app = Flask(__name__)


@app.route('/')
def main():
    in_path = request.args.get('file')
    out_path = os.path.join(gettempdir(), 'out.pdf')
    try:
        subprocess.run(
            # make sure `typst` is in $PATH
            ['typst', 'compile', in_path, out_path],
            check=True,
            capture_output=True,
        )
        return send_file(out_path, as_attachment=True)
    except subprocess.CalledProcessError as e:
        abort(500, f'Typst compile error: {e.stderr.decode()}')
    except Exception as e:
        abort(500, f'Server error: {e!s}')


if __name__ == '__main__':
    app.run(host='localhost', port=5000)
