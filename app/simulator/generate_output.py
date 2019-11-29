import json as _json


class GenerateOutput:

    def generate_output(self, output):
        with open('output.json', 'a+') as f:
            print('printing output..')
            f.write(_json.dumps(output))
            f.write('\n')
