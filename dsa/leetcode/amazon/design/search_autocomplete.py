from collections import defaultdict, OrderedDict


class AutocompleteSystem:
    class TreiNode:
        def __init__(self, val=None):
            self.val = ""
            if val is not None:
                self.val = val
            self.edges = {"end" : 0}

    def __init__(self, sentences, times):
        self.root = self.TreiNode()
        self.last_input = ""
        self.iter = self.root
        self.idx = 0

        for sentence, time in list(zip(sentences, times)):
            iter_ptr = self.root
            for char in list(sentence):
                new_node = self.TreiNode(iter_ptr.val + char)
                if char not in iter_ptr.edges:
                    iter_ptr.edges[char] = new_node
                iter_ptr = iter_ptr.edges[char]
            iter_ptr.edges["end"] = time


    def sort_by_ascii(self, sorted_retrievals):
        for i, (w, rets) in enumerate(sorted_retrievals.items()):
            if len(rets) > 1:
                sorted_retrievals[w] = sorted(rets, key=lambda word: [ord(c) for c in word[self.idx:]])



    def traverse(self, iter, retrieval):
        if "end" in iter.edges:
            retrieval[iter.edges["end"]].append(iter.val)

            if len(iter.edges) == 1:
                return

        for edge in iter.edges:
            if edge is not "end":
                self.traverse(iter.edges[edge], retrieval)


    def fetch_result_retrievals(self, all_retrievals):
        sorted_retrievals = OrderedDict({k: v for k, v in sorted(list(all_retrievals.items()), key=lambda x: x[0], reverse=True)})
        self.sort_by_ascii(sorted_retrievals)

        result = []
        items = []
        for k, v in sorted_retrievals.items():
            items.extend((k, v))
            result.extend(v)

        # print(items)

        return result[:3]


    def insert(self, entry):
        iter = self.root
        for c in entry:
            new_node = self.TreiNode(iter.val + c)
            if c not in iter.edges:
                iter.edges[c] = new_node
            iter = iter.edges[c]
        iter.edges["end"] += 1


    def input(self, c):
        all_retrievals = defaultdict(list)
        if c == '#':
            self.insert(self.last_input)
            self.iter = self.root
            self.last_input = ""
            self.idx = 0
            return []

        if c not in self.iter.edges or (self.iter == self.root and self.idx > 0):
            self.last_input += c
            self.idx += 1
            self.iter = self.root
            return []
        elif c in self.iter.edges:
            iter = self.iter
            self.traverse(iter.edges[c], all_retrievals)
            all_retrievals.pop(0, None)
            self.last_input += c
            self.idx += 1
            self.iter = self.iter.edges[c]

            if len(all_retrievals) == 0:
                return []

            return self.fetch_result_retrievals(all_retrievals)



# Your AutocompleteSystem object will be instantiated and called as such:
sentences = ["i love you","island", "i love xanadu", "i love leetcode", "i love iroman"]
times = [5,3,2,2,2]

sentences = ["i love you","island","iroman","i love leetcode"]
times = [5,3,2,2]

sentences = ["abc","abbc","a"]
times = [3,3,3]

# sentences = ["uqpewwnxyqxxlhiptuzevjxbwedbaozz","ewftoujyxdgjtazppyztom","pvyqceqrdrxottnukgbdfcr","qtdkgdbcyozhllfycfjhdsdnuhycqcofaojknuqqnozltrjcabyxrdqwrxvqrztkcxpenbbtnnnkfhmebj","jwfbusbwahyugiaiazysqbxkwgcawpniptbtmhqyrlxdwxxwhtumglihrgizrczv","cfptjitfzdcrhw","aitqgitjgrcbacgnaasvbouqsqcwbyskkpsnigtfeecmlkcjbgduban","utsqkmiqqgglufourfdpgdmrkbippffacwvtkpflzrvdlkdxykfpkoqcb","ethtbdopotpamvrwuomlpahtveyw","jiaqkaxovsqtkpdjfbkajpvpyetuoqwnrnpjdhoojbsdvneecsdvgqpyurmsvcy","j","btbnuplyeuccjbernsfbnveillrwdbqledwvpmvdbcugkurrkabtpykhlcogeszclyfuquafouv","hndjzblegevtfkgbjttektox","gtvnlninpvenapyfgmsjdisfnmiktitrutctawosjflvzfkbegnprixzqwzcyhoovsivuwmofsveqkyosowuyamuvy","sawrirvrfrbfagreahrioaombukmdwztbpggnxd","mgdcwptvbvhzyvvumvbjjn","otjvvkegwleyyxtghwgfmlsqlhrlibdvqfinyyebotjpwoaejhtornfgikmifdmwswbqgwhcbzuhrpajxuqicegcptszct","zlondsttyvnnnnxjtoqnlktitwzurissczzbyfsbgpoawodwjpsmavaugnhqtsbeixwl","yehvdehbtmwqkmcjmvpivfzqvevkotwzvjoyfvp","bjximtpayjdcxbrnksbtfnpynzaygygdflowewprqngdadzdhxcpgapjejojrkzrutgcsfpfvpluagniqimfqddldxqiw","bysyrxfykivyauysytgxfhqcrxliulahuizjvozpywrokxujhzpauxwufcxiitukljiiclatfrspqcljjoxpxziumstnhqr","uxtvutlgqapyfltiulwrplesmtowzoyhhjhzihatpuvmutxqgxfawpwypedbz","jzgsdjdawrqfladolduldhpdpagmvllvzamypuqlrpbmhxxadqaqrqavtxeghcyysjynovkiyjtvdluttodtmtocajgttmv","mbijfkmepalhdiubposdksdmmttxblkodcdrxbnxaqebnwliatnxpwaohbwkidia","ljggggbyxwrwanhjonoramexdmgjigrtpz","cqfvkutpipxjepfgsufonvjtotwfxyn","kvseesjazssavispavchdpzvdhibptowhyrrshyntpwkez","nveuzbaosuayteiozmnelxlwkrrrjlwvhejxhupvchfwmvnqukphgoacnazuoimcliubvhv","uwrpwhfdrxfnarxqpkhrylkwiuhzubjfk","bniyggdcloefwy","ihranmhbsahqjxesbtmdkjfsupzdzjvdfovgbtwhqfjdddwhdvrnlyscvqlnqpzegnvvzyymrajvso","lscreasfuxpdxsiinymuzybjexkpfjiplevqcjxlm","uwgnfozopsygnmptdtmmuumahoungpkodwxrcvfymqpeymaqruayvqqgoddgbnhemtsjifhxwiehncswxzrghf","nyfbxgcpfrzyqwfjzgmhuohjhrjizsyjqgmertmooeiaadcmiuyyylpcosnweoyydeauazhzbeaqn","tpylrxbwnkrfxckfdlvrbytaezuzmyscpvruthuvbxjenkeolvqsrjqzizyclzmqtjvnamdansmzyspcfghfprorqprua","nhldlmxpuckxeekipkrzugatjiivtazjbjyxokksyueyjbgmrovbckbxqcqefaiavzsarbbypgmpxe","sylraqsd","xr","xkzpxkhrucyatpatkigvntohihibyisyqtkjdhatdvyvxbjttz","nvnz","blzddwxphkgqfsfzfclwytstpvpzgcdeggdwzukzirscfzcteeuqbmmrfxcnokbbyxkqrxtjfarcefiynwfmy","inuxmuhtdwpuvyludwtokhtalxbuccepsayrjycbcwbtnfholjvkmypodv","awwillrm","xznodxngrstjrwqzmlmigpw","khlxjdtictufdfbkgfusdtaaeuspbbfmtjodflgqofzlqnulkdztflm","nlngmckslyqzjiyiexbropbxnynjcstziluewypboqhqndqsxhtnosrgrameajovsclrgwqjgnztvxrkhwnxkfrf","yroadxhxyacaexrwju","ujxlbpcbxdqrvubifnpzjmmkolyljzjhdegaiowaal","tnfnjgtxbckbpyplucprxcqzhrfjimylmlhdglntfydepltjvklyxesndzuubienhvuaqc","ouedhtkpkg","ygchsrrubucqffewifsxaefwocfaiiupqbomktvrcddggqfgnaycstpccwtbheyaqwhosxajqeqqxzyjsfng","jqqgpjvfkgjh","csowoazaiyejgyixszqmtctpzlkccccqregyhtvxccvrpkupwcyhqatxscevzdfbdqnuyadiyfnhysddfyxpgqtjiogmxsmzbbkr","dlzxdpchkdaztkqtrjmuujgoiae","plcjkwukkyqluxjbhxsyeaqvviinfuujsafwsquidvmutsrukxwrv","yopqbtpoqhpcktjangauzcvvpephhprpaaclbbkgchlqkrwdsaupeizlwxzcpkchoagmrrkwdkthosmrjefgbumnrjsb"]
# times = [12,9,4,4,1,5,3,4,7,9,2,4,2,3,11,13,1,3,4,10,7,1,9,5,10,14,5,3,2,11,5,14,4,13,11,5,15,8,1,12,2,11,4,2,11,14,9,12,1,7,13,11,7,2,6,10]

# sentences = ["pfeodi","a","imdphfjoncxvsakxgnzexnamuozxqgvnsbwsmlrouvkzrnmqqoykwadwkpniplbncbgfunzfjfodwapqwdfetlewszj","igqqgt","hcjfsnzyliljtwpbqllenrtcc","dvjpeulpixzericmekwfktseqifclxsxourvd","jroyhafuyvgigbfcobcamjeyqstgpvghgsyodihnbnralqiaavlupnmapvhm","ymlmgosaippwvmsnipbmxyarsfljpwuglccdks","lnueczsmseaqyhmboqwwcdktvqdteqtmmbpljxsotxvmt","pljxehadcsoyrbscydnthoincdockczclkeejnegqpwnjxwaomtlmtdvjxpk","xcnxqslkygflvcjmexgvwuylgrqwtruxurztmicuyodplojeofnikromqcdufwnvfccpolaeeocvncqxphxzlsjurrksn","eorlktlciabjipxchuateekvgosfbvjdltlorhcjwylzpogwbqftqxdkcsadizkvqoftvprecxujndrgudfrostkduhxpsihlcv","lqzxvnxwutloiypmwbunwgkijwqangcupqym","llvsygouwhwyqmayljygzdombwsysqzaryjyzzkzcdjksaghvmwyodqxepeujaelvxrxdrshoatpjexidbtr","scpacffopgtummidfytfpuebpuqkoftqxcoeexontgquvclifogyaibfrbishebtzjppkshaathtotzismjnjilexcemt","dempkwzpqerlfbpcevktzaouuoyoiewdnexbtaqxmsfruqwesbhcydjtllawxxyajuaxwpugxyc","ccgyonchgtkvgouysmnmqubkihgmfmwmlwdiijouuzlvsnltevtgrmlvptzxctqgymclsaaknzntxtctyh","ngfwqmfgxuscglalxmsgcwxrwjvvy","mbzdameiwljvshfhbxlylutqrczuievmaehbvcifcnriywo","chqsbbppkpkbbtxwxghocfrfmwufqeeyvibdpfkwtyedoljpxht","wkhqzrnhrojsrvckufgfxumzkcwcrbfioluwtymsggtcya","zaxjncdqtheiqcnheaqghavqffnibsxgqmovfzrkrdcnowltvruuczrzjhunpse","lrfllafxqsjapjcnkvebefxxjdkyfchfjakcnfyiweqbuvpeguqkgctvhznynsydohsmuuwqkeebzqtoufeccugmv","adykqjjethkumjhbiowyzfereuvrwrxpcxumwgohgyelmniltmdtayaqyqfwj","klepevabaezxdnjojklnisdfkbaouuuzlknkehbuu","tnjvjyztdbnyktccwgqxlggoyxkaozsnwujoanhvqgarombchffvxlxdfrzkhxzrsykymfbpqstwugpbazdxseyblniyi","hupooiqtfnydtihuszkpjwdlembpehznajeyujrpndtmhtqdszyczifcjstawxyqaoswlskitaat","rswmzniuorjz","grpomfwrsucjzrcnouyjsqqdtwgnbvdgrkozsnqzhsnpftegjckotvuqtwldaljojxlakjrvbah","toouoibwykiylsnpazmljuwmbouaerkuppphngmsxpqailglcgkxfbxbfjbozqgzkbljrkzaroogetopftevyvp","wtcsranprhywrwvcnzizqmhjslhwpozpcjsxmotihssskmszcudvgeutvcuzquceomxdlxavscuhntdz","ephzoc","qvglkxklktyyloutalevlfxcypzxciqkglrdxyylxyyqjwjhbhqo","omohendvivxaoaakeatafvgy","vjmyaartqnexagqagobjrjhgmgxyhmrmrrhbrdelipdzmbgznulmhsrtqyltacljlwpjtxhfjqnfqjns"]
# times = [10,14,7,3,6,3,6,11,12,12,4,10,12,6,3,13,1,12,7,6,9,5,1,4,5,5,4,14,10,6,11,10,7,3,13]


obj = AutocompleteSystem(sentences, times)



inputs = ["i"," ","l","o", "v", "e", " ", "#"]
inputs = ["i"," ","a", "#", "i"," ","a", '#', "i"," ","a", "#", "i"," ","a", "#"]
inputs = ["i"," ","a","#","i"," ","a","#","i"," ","a","#"]
inputs = ["w", "o", "f", "q", "m", "p", "k"]
inputs = ["b","c","#","b","c","#","a","b","c","#","a","b","c","#"]
# inputs = ["b", "k", "j", "o", "r", "d", "k"]
for input in inputs:
    # print(input, obj.input(input))
    print('{} : {}'.format(input, obj.input(input)))


# print(obj.input("w"))
