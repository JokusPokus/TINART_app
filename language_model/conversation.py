"""
Functionality for conversation management.
"""

import random
from typing import List

SETTINGS = {
    "politicians": {
        "lindner": {
            "aliases": ["christian", "lindner", "linder"]
        },
        "wagenknecht": {
            "aliases": ["sahra", "sarah", "sara", "wagenknecht", "waagenknecht"]
        }
    }
}


class Conversation:
    """
    Models a conversation by keeping track of conversation shares
    and lets bots answer if they are directly addressed.
    """
    def __init__(self, guests):
        """
        @param guests: Instance of the TalkshowGuests class (a dictionary containing
        the individual chatbots of all the guests)
        """
        self.guests = guests
        self.guest_list = list(guests.keys())

        # Keep track of number of utterances per guest and in total
        self.convo_log = {guest: 0 for guest in self.guest_list}
        self.total_utterances = 0

    @staticmethod
    def _alias_in_question(question: str, aliases: List[str]) -> bool:
        """
        Checks whether at least one of the given aliases is contained in the question.
        Case insensitive.

        @param question: Piece of text
        @param aliases: List of aliases that all refer to some politician
        @return: True if at least one alias is contained in the question, else False.
        """
        return bool([True for alias in aliases if alias in question.lower()])

    def _update_logs(self, speaker: str):
        """
        Updates the utterance logs w.r.t. to the current speaker.
        """
        self.convo_log[speaker] += 1
        self.total_utterances += 1

    def _addressed_guest(self, question):
        candidates = []
        for guest in self.guests:
            aliases = SETTINGS["politicians"][guest]["aliases"]
            if self._alias_in_question(question, aliases):
                candidates.append(guest)

        return random.choice(candidates) if candidates else None

    def _quiet_guest(self):
        if self.total_utterances == 0:
            return random.choice(self.guest_list)

        candidates = []
        probs_of_speaking = []

        for guest, share in self.convo_log.items():
            candidates.append(guest)
            prob = 1 - share / self.total_utterances
            probs_of_speaking.append(prob)

        return random.choices(candidates, weights=probs_of_speaking)[0]

    def _next_speaker(self, question):
        next_speaker = self._addressed_guest(question)

        if not next_speaker:
            next_speaker = self._quiet_guest()

        return next_speaker

    def next_utterance(self, question):
        next_speaker = self._next_speaker(question)
        self._update_logs(next_speaker)
        answer = self.guests[next_speaker].generate_response(question)

        return next_speaker, answer
