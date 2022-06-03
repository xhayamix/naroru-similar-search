<template>
   <div>

     <div class="row py-3 align-items-center">
      <div class="col-auto">
        <h1>小説検索</h1>
      </div>
      <div class="col">
        <input
          type="text"
          class="form-control"
          v-model="keyword"
          v-on:keydown.enter="search(keyword,1)"
        />
      </div>
      <div class="col-auto">
        <button class="btn btn-primary" v-on:click="search(keyword,1)">検索</button>
      </div>
    </div>
    <BasePagination 
      :showPages="showPages"
      :currentPage="currentPage"
      :totalCount="totalCount"
      :perPage="perPage"
      :totalPages="totalPages"
      @currentPage="getCurrentPage"
      v-if="list.length"
    ></BasePagination>

    <div v-for="novel in list" v-bind:key="novel.index">
      <div class="card mt-2 mb-2 bg-light">
        <div class="card-body">
          <h4 class="card-title"><router-link :to="'/novel/' + novel.index">{{ novel.title }}</router-link></h4>
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
      v-if="list.length"
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

      keyword : ""
    };
  },
  components: {
    BasePagination
  },
  methods: {
    //currentPageがページネーションコンポーネントから送られる現在のページ
    getCurrentPage(currentPage) {
      this.currentPage = currentPage;
      console.log(this.currentPage);
      //APIを呼び直す
      this.getData();
      window.scrollTo(0, 0);
    },
    //APIからのデータ取得
    search: async function(keyword, currentPage) {
      if (!keyword) {
        return;
      }
      this.currentPage = currentPage;
      this.keyword = keyword;
      this.getCount();
      this.getData();
    },
    getData: async function() {
      console.log(this.keyword)
      const response = await axios.get(process.env.VUE_APP_API_DEV + '/api/novel/get_by_keyword', {
          params: {
            page: this.currentPage,
            keyword: this.keyword
          }
        });
      
      this.list = [];
      response.data.forEach(element =>{
        this.list.push({
          index: element.index,
          title: element.title,
          general_lastup: element.general_lastup,
          writer: element.writer,
          ncode: element.ncode,
          story: element.story,
        })
      });
      
    },
    getCount: async function(){
      const count = await axios.get(process.env.VUE_APP_API_DEV + '/api/novel_by_keyword/count', {
          params: {
            keyword: this.keyword
          }
        });
      this.totalCount = count.data;
      this.totalPages = Math.ceil(parseInt(count.data, 10)/10);
    }
  },
};
</script>
 