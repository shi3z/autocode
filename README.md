# autocode ; Auto Python Code Generator

This program automatically generates Python code based on voice instructions. It captures a 5-second audio recording, interprets the instructions, and executes the generated code. The program has been tested and verified on macOS.

## Prerequisites

Before running the program, ensure that you have the following dependencies installed. You can install them using pip:

```bash
pip install sounddevice soundfile transformers anthropic
```

- `sounddevice`: Required for audio recording.
- `soundfile`: Required for saving and reading audio files.
- `transformers`: Required for audio transcription using the Whisper model.
- `anthropic`: Required for generating Python code using the Claude-3 API.

## Usage

1. Make sure you have the necessary dependencies installed (see [Prerequisites](#prerequisites)).

2. Set up your Anthropic API key:
   - Obtain an API key from Anthropic.
   - Set the `ANTHROPIC_API_KEY` environment variable with your API key.

3. Run the program:
   ```bash
   python autocode.py
   ```

4. The program will automatically start recording audio for 5 seconds.

5. Speak your instructions clearly during the recording period.

6. After the recording is complete, the program will transcribe the audio into text using the Whisper model.

7. The transcribed instructions will be sent to the Claude-3 API for generating Python code.

8. The generated Python code will be displayed in the console and saved to a file named `generated_code.py`.

9. The program will execute the generated code, and the output will be displayed in the console.

## Example

Here's an example of how to use the program:

1. Run the program:
   ```bash
   python autocode.py
   ```

2. Speak the following instruction during the recording period:
   ```
   Create a function that takes a list of numbers and returns the sum of all even numbers in the list.
   ```

3. The program will generate the corresponding Python code, which will be displayed in the console and saved to `generated_code.py`.

4. The generated code will be executed, and the output will be displayed in the console.

## Notes

- The program uses the default microphone for audio recording. Ensure that your microphone is properly configured and accessible.

- The quality of the generated code may vary depending on the clarity and precision of the spoken instructions.

- If the generated code requires additional dependencies or specific setup, make sure to handle them accordingly.

## License

This program is open-source and available under the [MIT License](LICENSE).
