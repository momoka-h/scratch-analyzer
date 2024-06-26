import sys
import json
import os
from collections import Counter

sys.path.append("../../")

from api import scratch_client
from api import drscratch_analyzer
import prjman
from prjman import ProjectManager

# # ２回派生した作品
sample_id = 971467755
# # １回派生した作品
sample_id2 = 971457785
# # リミックスしていない作品
sample_id3 = 732248801
# # サンプルプロジェクト
sample_id4 = 2767515787


# プロジェクトの大元のリミックス元とそこから何回派生しているか
# PM = scratch_client.get_remix_parent(sample_id2)
# if PM:
#     # print("parent_id: " + str(PM["parent_id"]))
#     # print("deep: " + str(PM["deep"]))
#     with open('data/test_PM_' + str(sample_id2) + '.json', 'w') as f:
#         json.dump(str(PM), f, indent=2)


# とりあえず何個取ってくるか後に設定する
# for id in range(276751787, 277751787):
    # MD = scratch_client.get_meta(id)

MD = scratch_client.get_meta(sample_id2)

# プロジェクトのメタ情報をとってくる
# parentが1個前
if MD:
    # print("metaData: " + str(MD))
    # jsonファイルに出力
    # with open('data/test_MD_' + str(sample_id2) + '.json', 'w') as f:
    #     json.dump(str(MD), f, indent=2)
    
    # リミックスしていたら1個前のプロジェクトのID出力
    # if MD["remix"]["parent"]:
    #     # print("parent_id: " + str(MD["remix"]["parent"]))
    #     with open('data/test_MD_' + str(sample_id2) + '.json', 'w') as f:
    #         json.dump(str(MD["remix"]["parent"]), f, indent=2)   
        # リミックスだった場合プロジェクトのjsonファイルの取得（リミックス前と後）
        
    # ブロック数を取得
    project_manager = ProjectManager(sample_id4)
    blocks_length = project_manager.get_blocks_length()
    # project = prjman.ProjectManager(sample_id)
    # blocks = project.prjman.get_blocks_length()
    # ブロックを取得
    #blockType = scratch_client.get_blocks(sample_id2)
    # スプライト数を取得
    # CTスコアを取得
    #CTscore = drscratch_analyzer.total_score(sample_id2)
    #CTscore = drscratch_analyzer.analyze(sample_id2)
    # 出力
    print("blocks count =" + blocks_length)
    #print("blockType =" + blockType)
    #print("CTscore = " + CTscore)


    #test
    #print(drscratch_analyzer.ct_score(sample_id2))

# リミックスだった場合のプロジェクトのCTScoreの取得（リミックス前と後）