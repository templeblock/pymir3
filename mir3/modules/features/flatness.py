import argparse
import copy

import mir3.data.feature_track as track
import mir3.data.spectrogram as spectrogram
import mir3.lib.mir.features as feats
import mir3.module

class Flatness(mir3.module.Module):
    """Spectral flatness track from a spectrogram"""

    def get_help(self):
        return """Spectral flatness of each frame of a spectrogram"""

    def build_arguments(self, parser):
        parser.add_argument('infile', type=argparse.FileType('rb'),
                            help="""file containing spectrogram""")
        parser.add_argument('outfile', type=argparse.FileType('wb'),
                            help="""output track file""")

    def calc_track(self, spectrum):
        return self.calc_track_band(spectrum,
                                    spectrum.freq_bin(spectrum.metadata.min_freq),
                                    spectrum.freq_bin(spectrum.metadata.max_freq))

    def calc_track_band(self, spectrum, min_freq_bin, max_freq_bin):
        t = track.FeatureTrack()
        t.data = feats.flatness(spectrum.data[min_freq_bin:max_freq_bin])
        t.metadata.sampling_configuration = spectrum.metadata.sampling_configuration
        t.metadata.feature = "Flatness_" + str(min_freq_bin) + "_" +\
            str(max_freq_bin)

        t.metadata.filename = spectrum.metadata.input.name
        t.metadata.input_metadata = copy.deepcopy(spectrum.metadata)

        return t

    def run(self, args):
        s = spectrogram.Spectrogram().load(args.infile)

        t = self.calc_track(s)

        # t = track.FeatureTrack()
        # t.data = feats.flatness(s.data)
        #
        # t.metadata.sampling_configuration = s.metadata.sampling_configuration
        # t.metadata.feature = "Flatness"
        # t.metadata.filename = s.metadata.input.name

        t.save(args.outfile)

