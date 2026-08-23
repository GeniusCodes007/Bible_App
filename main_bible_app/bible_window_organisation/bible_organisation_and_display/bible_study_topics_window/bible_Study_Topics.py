
class Bible_Study_Topics:
    def __init__(self):
        super().__init__()
        #self.topic = topic

    topics_list= { "Wisdom": [],
                     "Enlightenment": [],
                     "Strength": [],
                   "Stewardship": [""],
                   "Ancestry": ["Hebrews 7 vs 10"],
                   "Secrets of God Handed Unto Men": ["Matthew 2 vs 9 - 12", ],
                   "The Beatitudes": ["Matthew 5 vs 3 - 11"],
                   "Un-Repentance": ["Hebrews 6 vs 4 -6", "Hebrews 6 vs 7 - 8",],
                   "Repentance": [""],
                   "Fleeing From Sin": ["Matthew 5 vs 29 - 30"],
                   "Adultery and Lust": ["Matthew 5 vs 27 - 28", "Matthew 5 vs 31 - 32"],
                   "Divorce": ["Matthew 5 vs 31 - 32"],
                   "Oaths and Vows": ["Matthew 5 vs 33 - 37"],
                   "Tolerance and Revenge": ["Matthew 5 vs 38 - 42"],
                   "Those Doubting Christ": ["Matthew 12 vs 23",],
                   "The True Follower of Christ":["Matthew 12 vs 30"],
                   "The Sin Against The Holy Spirit": ["Matthew 12 vs 31 - 32"],
                   "Words of The Mouth": ["Matthew 12 vs 33 - 37", "Matthew 5 vs 22"],
                   "The Improvement of Every Teacher": ["Matthew 13 vs 52"],
                   "John the Baptist and Elijah": ["Matthew 17 vs 10 - 13"],
                   "Humility": ["Matthew 18 vs 1 - 5"],
                   "Agreement of Believers Between Heaven and Earth": ["Matthew 18 vs 18 - 20"],
                   "Forgiveness": ["Matthew 18 vs 21 - 35", "Matthew 5 vs 7"],
                   "Reconciliation": ["Matthew 5 vs 9", "Matthew 5 vs 23 - 26"],
                   "Eunuchs": ["Matthew 19 vs 10 - 12",],
                   "Purity of Thought": ["Matthew 5 vs 8", "Matthew 12 vs 33 - 35",],
                   "The Prophecies Fulfilled By Christ": ["Matthew 12 vs 17 - 21", "Matthew 13 vs 14 - 15", "Matthew 13 vs 35", "Matthew 21 vs 4 - 5"],
                   "Faith": ["Matthew 17 vs 19 - 21", "Matthew 21 vs 18 - 22"],
                   "Duties of Christ": ["Colossians 1 vs 20 - 23"],
                   "Christ, The Hope of Glory": ["Colossians 1 vs 27"],
                   "The Person of Christ": ["Colossians 1 vs 13 - 19", "Colossians 2 vs 2 - 3"],
                    "Deception In Faith": ["Matthew 18 vs 6 - 7", "Colossians 2 vs 4", "Colossians 2 vs 8"],
                   "Children In The Kingdom": ["Matthew 19 vs 13 - 15", "Matthew 21 vs 15 - 16", ]
                   }

    def show_topics(self)->list[str]:
        topics = []
        for topic in self.topics_list:
            print(topic)
            topics.append(topic)
        return topics

    def find_stuff(self, to_find:str=" "):
        for topic in self.topics_list:
            if to_find in topic:
                print(f"{to_find} is here in {topic}")

print(Bible_Study_Topics().find_stuff("Knowledge"))