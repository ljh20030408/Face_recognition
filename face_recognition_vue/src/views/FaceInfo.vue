<template>
  <div>
    <div style="margin-top: 2rem">
      <h1>
        人脸信息
      </h1>
    </div>
    <div>
      <el-table
          :data="infoData"
          style="width: 100%"
          :key="infoData.id"
      >
        <el-table-column
            fixed
            prop="ip"
            label="ip"
            width="150">
        </el-table-column>
        <el-table-column
            prop="name"
            label="姓名"
            width="120">
        </el-table-column>
        <el-table-column
            prop="time"
            label="时间"
            width="180">
        </el-table-column>
        <el-table-column
            fixed="right"
            label="操作"
            width="120">
          <template slot-scope="scope">
            <el-button
                size="mini"
                type="danger"
                @click="handleDelete(scope.row.id)">删除</el-button>
          </template>
        </el-table-column>
      </el-table>
      <div style="position: absolute; bottom: 15rem;left:45rem">
        <div class="block">
          <el-pagination
              @size-change="handleSizeChange"
              @current-change="handleCurrentChange"
              :current-page="currentPage"
              :page-sizes="[8]"
              :page-size="pageSize"
              layout="total, sizes, prev, pager, next, jumper"
              :total="totalSize">
          </el-pagination>
        </div>
      </div>

    </div>
  </div>
</template>

<script>
import {data} from "@tensorflow/tfjs";

export default {
  name: "FaceInfo",
  data: function (){
    return{
      infoData: [{
        id: '',
        ip: '',
        time: '',
        name: ''
      }],
      //初始页
      currentPage: 1,
      pageSize: 8,
      totalSize: 10
    }
  },
  methods: {
    getAll(){
      this.$axios.post("http://101.43.93.152:6006/info/getAll",{pageSize:this.pageSize,currentPage:this.currentPage}).then(
          res => {
            console.log(res)
            if (res.data.code == 0) {
              console.log(res.data)
              this.totalSize = res.data.data.total
              this.infoData = res.data.data.list
            }
          },
          err => {
            console.log(err)
          }
      )

    },
    handleDelete(id){
      this.$axios.get("http://101.43.93.152:6006/info/deleteById", {params:{id:id}}).then(
          res => {
            alert(res.data.data)
            window.location.reload()
          },
          err => {
            console.log(err)
          }
      )
    },
    handleSizeChange(val) {
      console.log(`每页 ${val} 条`);
    },
    handleCurrentChange(val) {
      this.currentPage = val
      this.getAll();
    }
  },
  mounted() {
    this.getAll()
  }
}
</script>

<style scoped>

</style>