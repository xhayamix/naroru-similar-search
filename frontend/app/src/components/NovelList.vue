<template>
  <div>
    <br>
    <h2 name="title" id="title">新着なろう</h2>
    <hr>

    <BasePagination 
      :showPages="showPages"
      :currentPage="currentPage"
      :totalCount="totalCount"
      :perPage="perPage"
      :totalPages="totalPages"
      @currentPage="getCurrentPage"
    ></BasePagination>

    <div v-for="novel in list" v-bind:key="novel.id">
      <div class="card mt-2 mb-2 bg-light">
        <div class="card-body">
          <h4 class="card-title"><router-link :to="'/novel/' + novel.id">{{ novel.title }}</router-link></h4>
          <h5 class="card-subtitle text-muted pl-3">作者：{{ novel.writer }}</h5>
          <div class='contenedor'>
            <input v-bind:id="novel.ncode" type="checkbox"/>
            <label v-bind:for="novel.ncode"></label>
            <div class="expand">
              <span class='content'>{{ novel.story }}</span>
              <br>
              <span class='content'>{{ novel.general_lastup }}</span>
            </div>
          </div>
        </div>
      </div>
    </div>
 
    <BasePagination 
      :showPages="showPages"
      :currentPage="currentPage"
      :totalCount="totalCount"
      :perPage="perPage"
      :totalPages="totalPages"
      @currentPage="getCurrentPage"
    ></BasePagination>


  </div>
</template>
 
<script>
import BasePagination  from "../components/BasePagination.vue";
import axios from 'axios';
 
export default {
  data() {
    return {
      //ページネーションの設定
      currentPage: 1, //現在のページ（初期は1）
      showPages: 5, //ページネーションを何ページ表示するか（奇数でないとずれる）
      perPage: 10, //1ページの表示件数
 
      //API用の設定
      totalCount: 0, //取得したアイテムの総件数
      totalPages: 0, //総ページ数
      list: [],
    };
  },
  components: {
    BasePagination
  },
  mounted() {
    this.getData();
    this.getCount();
  },
  methods: {
    //currentPageがページネーションコンポーネントから送られる現在のページ
    getCurrentPage(currentPage) {
      this.currentPage = currentPage;
      console.log(this.totalPages);
      //APIを呼び直す
      this.getData(currentPage);
      window.scrollTo(0, 0);
    },
    //APIからのデータ取得
    getData: async function(currentPage) {
      console.log(process.env.VUE_APP_API_DEV);
      const response = await axios.get(process.env.VUE_APP_API_DEV + '/api/novel/get_all', {
          params: {
            page: currentPage,
          }
        });
      
      this.list = [];
      console.log(response);
      response.data.forEach(element =>{
        this.list.push({
          id: element.id,
          title: element.title,
          general_lastup: element.general_lastup,
          writer: element.writer,
          ncode: element.ncode,
          story: element.story,
        })
      })
    },
    getCount: async function(){
      const count = await axios.get(process.env.VUE_APP_API_DEV + '/api/novel/count');
      this.totalCount = count.data;
      this.totalPages = Math.ceil(parseInt(count.data, 10)/10);
      console.log(this.totalPages);
    }
},
};
</script>
 
 <style>

 .contenedor {
   position:  relative;
 }
 .expand {/*全体*/
  width: auto;
  padding:0px 10px 10px;
  max-height: 80px;
  overflow: hidden;
  position: relative;
  border-bottom: 1px solid #aaa;
  transition: .5s;
}
 
.expand::before {/*グラデーション部分*/
    content: "";
    position: absolute;
    width: 100%;
    height: 50%;
    bottom: 0;
    background-image: linear-gradient(rgba(255, 255, 255, 0), #ffffff);
    pointer-events: none;
    transition: 1s;
}
 
.contenedor input {/*input要素は隠しておく*/
  visibility: hidden;
}
 
.contenedor label {/*ボタン部分のスタイル*/
  position: absolute;
  bottom: -.8em;
  display: block;
  font-size: .9em;
  padding: .20em 10px;
  right: 0;
  background: #aaa;
  box-shadow:-5px 0 white;
  color: white;
  z-index:999;
  cursor: pointer;
  text-transform: uppercase;
}
 
.contenedor label:before {/*閉じている際のボタンのテキスト*/
  content: "続きを読む";
}
 
.contenedor input:checked + label:before {/*開いているときは:checked状態なので、その際はボタンテキストを変える*/
  content: "閉じる"
}
 
input[type=checkbox]:checked ~ .expand {
 max-height: 500px;
}
 
input[type=checkbox]:checked ~ .expand:before {
 opacity: 0
}
 </style>