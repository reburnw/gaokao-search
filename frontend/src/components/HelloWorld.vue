<template>
  <v-container>
    <v-row class="text-center aligh-center">
      <v-card class="mx-auto" width="90%">
        <v-card-title>重庆市2019年高校录取信息查询</v-card-title>

        

        <v-container fluid>
          <div class="text-left">
      <v-dialog
        v-model="dialog"
        width="500"
      >
        <template v-slot:activator="{ on, attrs }">
          <v-btn
            color="red lighten-2"
            dark
            v-bind="attrs"
            v-on="on"
          >
            使用须知
          </v-btn>
        </template>
  
        <v-card>
          <v-card-title class="headline grey lighten-2">
            使用须知
          </v-card-title>
  
          <v-card-text>
            1. 本网站旨在为重庆市2020级考生高考考生提供客观数据参考，不以盈利为目的，不提供任何主观的志愿填报建议
            <br/>
            2. 本网站使用方式为：您可以搜索某一指定分数，网站会根据重庆考试院公布的录取信息，将所有包括该分数的录取信息展示给用户
            <br/> 
            例如：用户搜索“文史类 550分”，网站会将2019年公示的所有的[录取最高名次，录取最低名次]区间包括550分对应排名的文史类录取信息（院校）展示给用户
            <br/>
            请注意：展示出的信息仅仅代表“该院校在2019年重庆市该类别该批次的排位区间”与用户搜索的分数排位产生交集，网站不保证与2020年度录取有关的任何事宜
            <br/>
            3. 本网站所展示的所有数据均来自重庆市教育考试院官方网站，您可以在<a href="https://github.com/reburnw/gaokao-search/blob/master/origin_data/sites.txt">这个链接</a>下查看网站所有的数据源
            <br/>
            4. 因相关数据缺失，网站无法对部分高分与部分低分返回有效结果，敬请谅解
            <br/>
            5. 网站承诺不对用户的搜索记录做任何定制化的使用，您可以通过<a href="https://github.com/reburnw/gaokao-search">这个链接</a> 查看网站的开源代码实现，如您对网站有任何意见或者建议，您可以通过 reburnw@gmail.com 向开发者反馈
            
          </v-card-text>
  
          <v-divider></v-divider>
  
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn
              color="primary"
              text
              @click="dialog = false"
            >
              确认
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
    </div>
          <!-- v-radio-group label="查询方式" v-model="radios" :mandatory="false">
            <v-radio label="默认查询" value="1"></v-radio>
          </v-radio-group-->
          <v-switch v-model="switch1" :label="`类别: ${q_type1}`" color="grey"></v-switch>
          <v-text-field v-model="q_score" label="请输入查询的2020年高考分数(0-750的整数)"></v-text-field>
        </v-container>
        <v-container fluid></v-container>

        <!--v-card-text class="text--primary">
        
        <div>Whitehaven Beach</div>
  
        <div>Whitsunday Island, Whitsunday Islands</div>
        </v-card-text-->

        <v-card-actions>
          <v-btn color="primary"  @click="search()">查询</v-btn>
        </v-card-actions>
        <v-card-text class="text-left">
            2020年，{{q_score}}分对应的排名区间为[{{meta.high}},{{meta.low}}],位次对应的2019年高考分数大概为{{meta.related_score}}
          </v-card-text>
        <v-data-table
      :headers="headers"
      :items="desserts"
      :items-per-page="10"
      class="elevation-1"
    ></v-data-table>
      </v-card>
    </v-row>
  </v-container>
</template>

<script>

  export default {
    name: 'HelloWorld',


    data: () => ({
      switch1: false,
      radios: "1",
      q_score: "550",
      dialog: true,
      meta: {
        high: 0,
        low: 0,
        related_score: []
      },
      headers: [
        /*
         {
        "school_id": "1102",
        "school_name": "\u5317\u4eac\u5927\u5b66\u533b\u5b66\u90e8",
        "count": "6",
        "type1": "\u7406\u5de5\u7c7b",
        "type2": "1\u5fd7\u613f",
        "high_score": 680,
        "low_score": 673,
        "origin": "http://www.cqksy.cn/site/infopub/2019/gk/zhengji/071103.htm",
        "info_type": "\u672c\u79d1\u63d0\u524d\u6279"
        },
        */
        {
          text: '学校名称',
          align: 'start',
          sortable: false,
          value: 'school_name',
        },
        { text: '录取批次', value: 'info_type' },
        { text: '录取人数', value: 'count' },
        { text: '科类', value: 'type1' },
        { text: '录取志愿', value: 'type2' },
        { text: '最低分', value: 'low_score' },
        { text: '最高分', value: 'high_score' },
      ],
      desserts: [
        
      ],
    
    }),
    computed: {
      q_type1: function() {
        if(!this.switch1) {
          return "文史类"
        } else {
          return "理工类"        }
      }
    },
    methods: {
      search: function(){
        
        this.q_score = parseInt(this.q_score);
        
        if(isNaN(this.q_score)){
          alert("请输入正整数分数");
          this.q_score=600;
          return;
        }
        //console.log(this.q_type1);
        
        var q_type1_string="";
        if(!this.switch1){
          q_type1_string = "&q_type1=文史类";
        } else {
          q_type1_string = "&q_type1=理工类";
        }
        var q_score_string="&q="+this.q_score;
        var q_string = "q_type=1"+q_type1_string+q_score_string;
        var that = this;
        this.$http.get('/api/q?'+q_string).then(function(res){
            //console.log(res.data.data);
            that.desserts = res.data.data;
            that.meta = res.data.meta;
        })
        
        return ;
      }
    }
  }
</script>
