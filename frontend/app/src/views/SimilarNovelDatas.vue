<template>
  <div>
    <h2 class="mb-2" id="top" v-cloak>類似検索</h2>
    <small>{{novel.ncode}}</small>
    <h3 class="mb-5"><router-link :to="'/novel/' + novel.id">{{novel.title}}</router-link></h3>

    <div v-for="(novel, index) in similarlist" v-bind:key="novel.id">
      <div class="card mt-2 mb-2 bg-light">
        <div class="card-body">
          <h4 class="card-title"><router-link :to="'/novel/' + novel.id">{{index + 1}}：{{ novel.title }}</router-link></h4>
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
    <a href="#top" v-if="similarlist.length > 0">ページトップへ</a>

  </div>
</template>
 
<script>

import axios from 'axios';
 
export default {
  data() {
    return {
      novel: [],
      similarlist: [],
    };
  },
  mounted() {
    this.id = this.$route.params.id;
    this.getData();
  },
  methods: {
    //APIからのデータ取得
    getData: async function() {
        let currentid = this.id -1;
        let url = process.env.VUE_APP_API_DEV + '/api/siminovel/get/' + currentid;
        const response = await axios.get(url);
        console.log(response.data[0][0]);
        for(let i = 0;i < 10;i++){
            let id = response.data[i][0] - 1;
            url = process.env.VUE_APP_API_DEV + '/api/novel/get/' + id;
            let simiresponse = await axios.get(url);
            this.similarlist.push(simiresponse.data[0]);
        }
        url = process.env.VUE_APP_API_DEV + '/api/novel/get/' + this.id;
        const currentresponse = await axios.get(url);
        this.novel =currentresponse.data[0];
    },
},
};
</script>

<style>
h3 {
  margin-bottom: 0.5em;
  border-bottom: 0.5px solid #999696;
  line-height: 1.7em;
}
</style>