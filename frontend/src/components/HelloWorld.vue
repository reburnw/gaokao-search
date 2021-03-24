<template>
  <v-container>
    <v-row class="text-center aligh-center">
      <v-card class="mx-auto" width="90%">
        <v-card-title>神秘网站</v-card-title>

        

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
            神秘网站使用须知
          </v-btn>
        </template>
  
        <v-card>
          <v-card-title class="headline grey lighten-2">
            使用须知
          </v-card-title>
  
          <v-card-text>
            咕咕咕咕咕
            
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
          <v-text-field v-model="q_score" label="请输入查询的故事线id(1-5的整数)"></v-text-field>
        </v-container>
        <v-container fluid>
          <h4>{{ desserts }}</h4>
        </v-container>

        <!--v-card-text class="text--primary">
        
        <div>Whitehaven Beach</div>
  
        <div>Whitsunday Island, Whitsunday Islands</div>
        </v-card-text-->

        <v-card-actions>
          <v-btn color="primary"  @click="search()">查询</v-btn>
        </v-card-actions>
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
      q_score: "1",
      dialog: false,
      desserts: {},
    
    }),
    computed: {
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

        var q_score_string="&q_id="+this.q_score;
        var q_string = "q_type=1"+q_score_string;
        var that = this;
        this.$http.get('/api/q?'+q_string).then(function(res){
            console.log(res.data.data);
            that.desserts = res.data.data;
            //that.meta = res.data.meta;
        })
        
        return ;
      }
    }
  }
</script>
