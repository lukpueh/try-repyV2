"""
<Program Name>
  upper_dot_lower.py

<Started>
  March, 2017

<Author>
  Lukas Puehringer <lukas.puehringer@nyu.edu>

<Purpose>
  Provides functions to encode and decode to and from dot-lower encoding.
  Dot-lower encoding replaces all upper case letters in a string
  with a dot followed by the lower case representation of that letter.
  Additionally, the encoding prepends an underscore.

  This module can be used to generate RepyV2 conformant non-hidden filenames
  from base64 encoded strings.

  Note:
  The module can be used as Python or RepyV2 module.

<Example>
  >>> base64_enc = "c3lzdGVtanMvYWNlL3JlbmFtLnNo"
  >>> dot_lower_enc = encode_dot_lower(base64_enc)
  >>> dot_lower_enc
  '_c3lzd.g.vtan.mv.y.w.nl.l3.jlbm.ft.ln.no'
  >>> dot_lower_dec = decode_dot_lower(dot_lower_enc)
  >>> base64_enc == dot_lower_dec
  True

"""

def encode_dot_lower(string):
  """
  <Purpose>
    Dot-lower encodes a passed string by replacing all upper case letters
    with a dot (.) and the lower case representation of that string.
    Additionally the encoder prepends an underscore (_).

  <Arguments>
    string
      A string to dot-lower encode

  <Returns>
    A dot lower encoded version of the passed string

  """
  string_enc = "_"

  for char in string:
    if char.isupper():
      char_enc = "." + char.lower()

    else:
      char_enc = char

    string_enc += char_enc

  return string_enc


def decode_dot_lower(string_enc):
  """
  <Purpose>
    Decodes a passed dot-lower encoded string by replacing all
    all dots (.) and the succeeding lower case letter with the upper case
    representation of that letter.
    The first letter is ignored, because it should be an underscore (_).


  <Arguments>
    sting_enc
      A string to dot-lower decode

  <Returns>
    The dot lower decoded version of the passed string

  """
  string_dec = ""
  length = len(string_enc)

  # Start at 1 to ignore the leading underscore
  i = 1
  while i < length:
    if (string_enc[i] == "." and i + 1 < length and
        string_enc[i + 1].isalpha()):
      string_dec += string_enc[i + 1].upper()
      i += 2

    else:
      string_dec += string_enc[i]
      i += 1

  return string_dec
