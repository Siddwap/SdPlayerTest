// Change the second argument to your options:
// https://github.com/sampotts/plyr/#options
const controls = [
              'play-large', // The large play button in the center
	      'rewind', // 10 seconds rewind
              'play', // Play/pause playback
	      'fast-forward', //10 Second forward
              'progress', // The progress bar and scrubber for playback and buffering
              'current-time', // The current time of playback
              'duration', // The full duration of the media
              //'mute', // Toggle mute
              //'volume', // Volume control
              //'captions', // Toggle captions
              'settings', // Settings menu
              'pip', // Picture-in-picture (currently Safari only)
              'airplay', // Airplay (currently Safari only)
              'download', // Show a download button with a link to either the current source or a custom URL you specify in your options
              'fullscreen' // Toggle fullscreen
               ];
            var defaultOptions = {
			    controls,
                "autoplay": false,
                "muted": false,
                "loop": {
                    "active": false
                },
                "captions": {
                    "active": true,
                    "update": true
                }
            };
            defaultOptions.tooltips = {controls: true, seek:true};
            defaultOptions.quality = {
                            default: "default"
                        };
const player = new Plyr('video', defaultOptions, { captions: { active: true }, ads: { enabled: true, tagUrl: 'https://syndication.realsrv.com/splash.php?idzone=4774980' } });

// Expose player so it can be used from the console
window.player = player;
Footer
© 2022 GitHub, Inc.
Footer navigation
Terms
