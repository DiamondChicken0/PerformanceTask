from synthesizer import Player, Synthesizer, Waveform

player = Player()
player.open_stream()

print("play major chord")
synthesizer = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)
chord = ["C4", "E4", "G4"]
player.play_wave(synthesizer.generate_chord(chord, 3.0))