from spacy.en import English

parser = English()

class SpacyTagger:

    def __init__(self, sentence):
        self.sentence = sentence

class SpacyParser:

    def __init__(self, tagger):
        self.tagger = tagger
        self.parser = parser

    def execute(self):
        parsed = self.parser(self.tagger.sentence)
        edges = []
        names = []
        words = []
        tags = []
        types = []
        
        i = 0
        items_dict = dict()
        for item in parsed:
            items_dict[item.idx] = i
            i += 1

        for item in parsed:
            index = items_dict[item.idx]
            for child_index in [items_dict[l.idx] for l in item.children]:
                edges.append((index, child_index))
            names.append("v" + str(index))
            words.append(item.vector)
            tags.append(item.tag_)
            types.append(item.dep_)
        
        return names, edges, words, tags, types


    def execute_backward(self):
        parsed = self.parser(self.tagger.sentence)
        edges = []
        names = []
        words = []
        tags = []
        types = []
        
        i = 0
        items_dict = dict()
        for item in parsed:
            items_dict[item.idx] = i
            i += 1

        for item in parsed:
            index = items_dict[item.idx]
            for child_index in [items_dict[l.idx] for l in item.children]:
                edges.append((child_index, index))
            names.append("v" + str(index))
            words.append(item.vector)
            tags.append(item.tag_)
            types.append(item.dep_)

        return names, edges, words, tags, types
