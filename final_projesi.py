import networkx as nx
import pandas as pd
from networkx.algorithms import community

file_path = 'bayburt_ilceleri.csv'
data = pd.read_csv(file_path, header=None, names=["Koy1", "Koy2", "Mesafe"])

G = nx.Graph()

for index, row in data.iterrows():
    G.add_edge(row["Koy1"], row["Koy2"], weight=float(row["Mesafe"]))

nokta_sayisi = G.number_of_nodes()
kenar_sayisi = G.number_of_edges()
ortalama_derece = sum(dict(G.degree()).values()) / float(nokta_sayisi)

en_kisa_yollar = dict(nx.all_pairs_dijkstra_path_length(G, weight='weight'))

derece_merkeziyeti = nx.degree_centrality(G)
ortadalik_merkeziyeti = nx.closeness_centrality(G)
yakinlik_merkeziyeti = nx.betweenness_centrality(G)
ozvektor_merkeziyeti = nx.eigenvector_centrality(G, max_iter=1000)

en_yuksek_derece_merkeziyeti = sorted(derece_merkeziyeti.items(), key=lambda x: x[1], reverse=True)[:5]
en_yuksek_ortadalik_merkeziyeti = sorted(ortadalik_merkeziyeti.items(), key=lambda x: x[1], reverse=True)[:5]
en_yuksek_yakinlik_merkeziyeti = sorted(yakinlik_merkeziyeti.items(), key=lambda x: x[1], reverse=True)[:5]
en_yuksek_ozvektor_merkeziyeti = sorted(ozvektor_merkeziyeti.items(), key=lambda x: x[1], reverse=True)[:5]

topluluklar = community.girvan_newman(G)
ilk_topluluklar = next(topluluklar)

topluluk_listesi = [sorted(list(grup)) for grup in ilk_topluluklar]

sonuclar_df = pd.DataFrame({
    "Metrik": ["Nokta Sayısı", "Kenar Sayısı", "Ortalama Derece"],
    "Değer": [nokta_sayisi, kenar_sayisi, ortalama_derece]
})

en_kisa_yollar_df = pd.DataFrame(en_kisa_yollar).map(lambda x: dict(x) if isinstance(x, dict) else x)

# Sonuçları yazdır
print("Ağ Metrikleri")
print(sonuclar_df)
print("\nEn Kısa Yol Uzunlukları")
print(en_kisa_yollar_df)

en_yuksek_derece_merkeziyeti = [node for node, centrality in en_yuksek_derece_merkeziyeti]
en_yuksek_ortadalik_merkeziyeti = [node for node, centrality in en_yuksek_ortadalik_merkeziyeti]
en_yuksek_yakinlik_merkeziyeti = [node for node, centrality in en_yuksek_yakinlik_merkeziyeti]
en_yuksek_ozvektor_merkeziyeti = [node for node, centrality in en_yuksek_ozvektor_merkeziyeti]

print("\nEn Yüksek Derece Merkeziyetine Sahip Köyler:")
print(en_yuksek_derece_merkeziyeti)

print("\nEn Yüksek Ortadalık Merkeziyetine Sahip Köyler:")
print(en_yuksek_ortadalik_merkeziyeti)

print("\nEn Yüksek Yakınlık Merkeziyetine Sahip Köyler:")
print(en_yuksek_yakinlik_merkeziyeti)

print("\nEn Yüksek Özvektör Merkeziyetine Sahip Köyler:")
print(en_yuksek_ozvektor_merkeziyeti)

print("\nTopluluklar:")
for i, topluluk in enumerate(topluluk_listesi):
    print(f"Topluluk {i + 1}: {topluluk}")
