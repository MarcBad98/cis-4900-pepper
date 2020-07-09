# Extending the `requests` package

After learning that `requests` is available on Pepper's local machine, the first capability to try to enhance was her speech-to-text functions. Currently, Pepper has a built-in speech-to-text engine that only allows recognition of words from a pre-defined list (using pattern matching). To circumvent defining a set vocabulary, developers can take advantage of Cloud computing and services.

## Echo

This Choregraphe project is a small project that uses [Google Cloud Speech-to-Text API](https://cloud.google.com/speech-to-text) to transcribe audio files to text. It provides another small demonstration of how REST calls can improve Pepper's usability.

<img src="Echo/icon.png" width="10%" height="10%" />

## Goals

- [x] Get sound and text from Pepper's microphone(s)
- [x] Output sound and speech

## Choregraphe Project Canvas

![Choregraphe Project Canvas](docs-echo-project.PNG)

## Challenges

Even though Choregraphe provides several built-in boxes with pre-defined functions, this does not mean that the developer is constrained to those functionalities. These built-in boxes are essentially Python box scripts that are specialized for one task. By understanding the Python that the boxes run, developers can modify these built-in boxes for their own needs. Take the following example:

<img src="docs-unmodified-record-sound-box.PNG" />

The image above shows the inner workings of an unmodified _record sound_ Choregraphe box. From the developer-set parameters, this box first retrieves the audio file's name. The box then starts recording audio and activates the _wait_ Choregraphe box, which activates its output after a specified amount of time. By analyzing this structure, see that this entire box records audio for a pre-determined time. But what if we wanted to record audio for an unspecified amount of time? Rather than starting from scratch, this Choregraphe box can be modified to achieve our goal.

<img src="docs-modified-record-sound-box.PNG" />

The image above shows the inner workings of the modified _record sound_ Choregraphe box in the Echo Choregraphe project. See that rather than the _wait_ Choregraphe box determining when the recording will stop, we instead added a new input to this box which directly stops the recording. In the Echo project, when the human says "Over", the recording is terminated and the audio file saved.

## Code

<details><summary>Google STT Cloud Service Python Box Script</summary>

```python
class MyClass(GeneratedClass):
    def __init__(self):
        GeneratedClass.__init__(self)
        self.tts = ALProxy('ALTextToSpeech')

    def onLoad(self):
        pass

    def onUnload(self):
        pass

    def onInput_onStart(self, file_path):
        import json
        import base64
        import requests

        # setup the JSON payload for the Google Speech-to-text Cloud service
        audio = open(file_path, 'rb')
        config = {
            "config": {
                "encoding": "LINEAR16",
                "languageCode": "en-US"
            },
            "audio": {
                "content": base64.b64encode(audio.read())
            }
        }
        audio.close()

        # make the API call

        # UPDATE: 2020-07-02, it seems Google has changed how the API is accessed,
        # which breaks this Python code :(

        # WARNING: I hard-coded the API key into the endpoint;
        # when I disable the API (since it could cost me money), this endpoint will die

        r = requests.post('https://speech.googleapis.com/v1/speech:recognize?key=AIzaSyA0Ab_PzouKaLkNJvgusszirtHPC8uniXU', json=config)
        self.logger.info(r)
        data = json.loads(r.text)

        # extract and echo the human's speech
        text = data['results'][0]['alternatives'][0]['transcript']
        self.tts.say('You said this: {}'.format(text))

        # stop the program
        self.onStopped()

    def onInput_onStop(self):
        self.onUnload()
        self.onStopped()
```

</details>
