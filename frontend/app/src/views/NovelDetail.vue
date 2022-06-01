<template>
<div>
  <small>{{novel.ncode}}</small>
  <h1 class="detailtitle">{{novel.title}}</h1>
  <div class="mb-2">
    <span class="mr-3" id="noveltype" v-if="novel.end === 1">連載中</span>
    <span class="mr-3" id="noveltype" v-else-if="novel.novel_type === 1">完結</span>
    <span class="mr-3" id="noveltype" v-else>短編</span>
    <a class="mr-3" v-bind:href="'https://ncode.syosetu.com/' + novel.ncode" target="_blank">小説を読む</a>
    <a class="mr-3" href="">類似作品検索</a>
  </div>
  <div class="card mt-2 mb-2 bg-light">
    <div class="card-body">
      <h4 class="card-title text-danger">あらすじ</h4>
      <h5 class="card-text pl-3">{{novel.story}}</h5>
    </div>
  </div>
  <div class="card mt-2 mb-2 bg-light">
    <div class="card-body">
      <h4 class="card-title text-danger">作者</h4>
      <h5 class="card-text pl-3">{{novel.writer}}</h5>
    </div>
  </div>
  <div class="card mt-2 mb-2 bg-light">
    <div class="card-body">
      <h4 class="card-title text-danger">キーワード</h4>
      <h5 class="card-text pl-3">{{novel.keyword}}</h5>
    </div>
  </div>
  <div class="card mt-2 mb-2 bg-light">
    <div class="card-body">
      <h4 class="card-title text-danger">ジャンル</h4>
      <h5 class="card-text pl-3" v-if="novel.genre === 101">異世界〔恋愛〕</h5>
      <h5 class="card-text pl-3" v-else-if="novel.genre === 102">現実世界〔恋愛〕</h5>
      <h5 class="card-text pl-3" v-else-if="novel.genre === 201">ハイファンタジー〔ファンタジー〕</h5>
      <h5 class="card-text pl-3" v-else-if="novel.genre === 202">ローファンタジー〔ファンタジー〕</h5>
      <h5 class="card-text pl-3" v-else-if="novel.genre === 301">純文学〔文芸〕</h5>
      <h5 class="card-text pl-3" v-else-if="novel.genre === 302">ヒューマンドラマ〔文芸〕</h5>
      <h5 class="card-text pl-3" v-else-if="novel.genre === 303">歴史〔文芸〕</h5>
      <h5 class="card-text pl-3" v-else-if="novel.genre === 304">推理〔文芸〕</h5>
      <h5 class="card-text pl-3" v-else-if="novel.genre === 305">ホラー〔文芸〕</h5>
      <h5 class="card-text pl-3" v-else-if="novel.genre === 306">アクション〔文芸〕</h5>
      <h5 class="card-text pl-3" v-else-if="novel.genre === 307">コメディー〔文芸〕</h5>
      <h5 class="card-text pl-3" v-else-if="novel.genre === 401">VRゲーム〔SF〕</h5>
      <h5 class="card-text pl-3" v-else-if="novel.genre === 402">宇宙〔SF〕</h5>
      <h5 class="card-text pl-3" v-else-if="novel.genre === 403">空想科学〔SF〕</h5>
      <h5 class="card-text pl-3" v-else-if="novel.genre === 404">パニック〔SF〕</h5>
      <h5 class="card-text pl-3" v-else-if="novel.genre === 9901">童話〔その他〕</h5>
      <h5 class="card-text pl-3" v-else-if="novel.genre === 9902">詩〔その他〕</h5>
      <h5 class="card-text pl-3" v-else-if="novel.genre === 9903">エッセイ〔その他〕</h5>
      <h5 class="card-text pl-3" v-else-if="novel.genre === 9904">リプレイ〔その他〕</h5>
      <h5 class="card-text pl-3" v-else-if="novel.genre === 9999">その他〔その他〕</h5>
      <h5 class="card-text pl-3" v-else>ノンジャンル〔ノンジャンル〕</h5>
    </div>
  </div>

  <div id="similar-button" v-cloak>
    <a href=""><router-link :to="'/siminovel/get/' + novel.id">類似検索</router-link></a>
  </div>

  <div class="d-flex justify-content-between mt-3">
    <div class="bd-highlight">
      <h3>日時関連</h3>
      <ul class="list-unstyled">
        <ul class="list-inline">
          <li class="list-inline-item">初回掲載日：</li>
          <li class="list-inline-item">{{novel.general_firstup}}</li>
        </ul>
        <ul class="list-inline">
          <li class="list-inline-item">最終掲載日：</li>
          <li class="list-inline-item">{{novel.general_lastup}}</li>
        </ul>
        <ul class="list-inline">
          <li class="list-inline-item">小説更新日：</li>
          <li class="list-inline-item">{{novel.novelupdated_at}}</li>
        </ul>
      </ul>
    </div>
    <div class="bd-highlight">
      <h3>詳細情報</h3>
      <ul class="list-unstyled">
        <ul class="list-inline">
          <li class="list-inline-item">話数：</li>
          <li class="list-inline-item">{{novel.general_all_no}}</li>
        </ul>
        <ul class="list-inline">
          <li class="list-inline-item">文字数：</li>
          <li class="list-inline-item">{{novel.length}}</li>
        </ul>
        <ul class="list-inline">
          <li class="list-inline-item">読了時間(分単位)：</li>
          <li class="list-inline-item">{{novel.time}}</li>
        </ul>
        <ul class="list-inline">
          <li class="list-inline-item">ブックマーク数：</li>
          <li class="list-inline-item">{{novel.fav_novel_cnt}}</li>
        </ul>
      </ul>
    </div>
    <div class="bd-highlight">
      <h3>評価情報</h3>
      <ul class="list-unstyled">
        <ul class="list-inline">
          <li class="list-inline-item">総合ポイント：</li>
          <li class="list-inline-item">{{novel.global_point}}</li>
        </ul>
        <ul class="list-inline">
          <li class="list-inline-item">日間ポイント：</li>
          <li class="list-inline-item">{{novel.daily_point}}</li>
        </ul>
        <ul class="list-inline">
          <li class="list-inline-item">週間ポイント：</li>
          <li class="list-inline-item">{{novel.weekly_point}}</li>
        </ul>
        <ul class="list-inline">
          <li class="list-inline-item">月間ポイント：</li>
          <li class="list-inline-item">{{novel.monthly_point}}</li>
        </ul>
        <ul class="list-inline">
          <li class="list-inline-item">四半期ポイント：</li>
          <li class="list-inline-item">{{novel.quarter_point	}}</li>
        </ul>
        <ul class="list-inline">
          <li class="list-inline-item">年間ポイント：</li>
          <li class="list-inline-item">{{novel.yearly_point}}</li>
        </ul>
      </ul>
    </div>
  </div>



  
  

</div>

  



</template>
 
<script>
//import BasePagination  from "../components/BasePagination.vue";
import axios from 'axios';
 
export default {
  data() {
    return {
      novel: [],
      id: 1
    };
  },
  mounted() {
    this.id = this.$route.params.id;
    this.getNovel();
  },
  methods: {
    //APIからのデータ取得
    getNovel: async function() {
        let url = process.env.VUE_APP_API_DEV + '/api/novel/get/' + this.id;
        const response = await axios.get(url);
        this.novel =response.data[0];
    }
  },
};
</script>

<style>
.detailtitle {
  border-bottom: 0.5px solid #999696;
  line-height: 1.7em;
}

#noveltype{
  margin: 0px, 8px, 0px, 0px;
  padding: 3px, 5px;
  color: #fafafa;
  background: #333333;
  border: 1px solid #666666;
  text-align: center;
}

#similar-button{
  margin: 30px auto 30px auto;
  width: 200px;
  border: 1px solid;
  border-color: #CCCCCC #666666 #666666 #CCCCCC;
}

#similar-button a{
  font-weight: bold;
  display: block;
  text-align: center;
  font-size: 140%;
  color: #444444;
  background: #cceedd;
  border: 1px solid;
  border-color: #ffffff;
}
</style>
 