import argparse
import numpy

import mir3.data.score as score
import mir3.lib.mir.midifeatures as feats
import mir3.module

class Intervals(mir3.module.Module):
    """Calculates the interval histogram from a score"""

    def get_help(self):
        return """Pitch class histogram from a score. Prints the values on
    screen"""

    def build_arguments(self, parser):
        parser.add_argument('infile', type=argparse.FileType('rb'),
                            help="""file containing score""")

    def run(self, args):
        s = score.Score().load(args.infile)
        events = feats.event_list(s.data)
        histogram = feats.interval_histogram(events)
        for i in xrange(12):
            print histogram[i],
        print " "


