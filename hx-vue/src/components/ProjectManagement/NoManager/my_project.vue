<template>
  <div>
    <div class="project_table">
      <el-table
        :data="
          projects.slice(
            (this.currentPage - 1) * pagesize,
            this.currentPage * pagesize
          )
        "
        style="width:100%"
        stripe
        @filter-change="filterTagTable"
      >
        <el-table-column label="项目id" prop="id" sortable></el-table-column>
        <el-table-column
          label="项目名称"
          prop="name"
          sortable
        ></el-table-column>
        <el-table-column
          label="项目状态"
          prop="status"
          column-key="status"
          :filters="filter_status"
          filter-placement="bottom-end"
        >
          <template slot-scope="props">
            <zx-tag :type="FlowStatusRules[props.row.status]">
              {{ FLOWS_STATUS[props.row.status] }}
            </zx-tag>
          </template>
        </el-table-column>
        <el-table-column
          label="更新时间"
          prop="update_time"
          :sortable="true"
          :sort-method="sortByDate"
        ></el-table-column>
        <el-table-column
          label="remain时间"
          prop="remain_work_time"
          :sortable="true"
          :sort-method="sortByDate"
        ></el-table-column>
        <el-table-column label="操作">
          <template slot-scope="scope">
            <el-button
              size="mini"
              @click="handleEdit(scope.$index, scope.row)"
              :disabled="setButtonFlag(scope.row)"
              >查看工时</el-button
            >
          </template>
        </el-table-column>
      </el-table>
      <el-row class="pag">
        <el-pagination
          @current-change="handleCurrentChange"
          :current-page="currentPage"
          :page-size="pagesize"
          :total="projects.length"
        >
        </el-pagination>
      </el-row>
    </div>
    <edit-form
      :show.sync="dialogFormVisible"
      :zid="tmpId"
      @updateAgain="getAllProjects"
      ref="edit"
    ></edit-form>
  </div>
</template>

<script>
import EditForm from './project_editForm'
import SideMenu from './NoManger_SideMenu'
import { FlowStatusRules } from '../../home/rule/data-config'
import ZxTag from '../../tag'
export default {
  name: 'ManagerRAudit',
  components: {
    'side-menu': SideMenu,
    'zx-tag': ZxTag,
    'edit-form': EditForm
  },
  data () {
    return {
      buttonFlag: false,
      select: '',
      tmpId: '-1',
      dialogFormVisible: false,
      uid: 0,
      career: -1,
      tableDataTmp: [],
      currentPage: 1,
      pagesize: 5,
      total: 10,
      FlowStatusRules,
      filter_status: [
        { text: 'rejection', value: 0 },
        { text: 'pending', value: 1 },
        { text: 'established', value: 2 },
        { text: 'processing', value: 3 },
        { text: 'paid', value: 4 },
        { text: 'finished', value: 5 },
        { text: 'archived', value: 6 }
      ],
      FLOWS_STATUS: [
        'rejection',
        'pending',
        'established',
        'processing',
        'paid',
        'finished',
        'archived'
      ],
      projects: [
        {
          id: '',
          name: '',
          'status': '',
          update_time: '',
          remain_work_time: ''
        }
      ]
    }
  },
  methods: {
    setButtonFlag (row) {
      if (!this.projects[row.id]) {
        return false
      }
      // eslint-disable-next-line eqeqeq
      if (this.projects[row.id].status == 0) {
        return true
      }
      return false
    },
    getAllInfo () {
      let _this = this
      this.$axios
        .get('/project/work_time', {
          params: {
            uid: _this.uid,
            project_id: _this.tmpId
          }
        })
        .then(successResponse => {
          _this.$refs.edit.form = successResponse.data
          _this.$refs.edit.form.status = _this.FLOWS_STATUS[successResponse.data.status]
        })
    },
    handleEdit (index, row) {
      this.$refs.edit.form = {
        id: row.id
      }
      this.tmpId = row.id
      this.$refs.edit.form.id = row.id
      this.getAllInfo()
      this.dialogFormVisible = true
    },
    filterTagTable (filters) {
      this.projects = this.tableDataTmp
      // eslint-disable-next-line eqeqeq
      if (filters.status.length == 0) {
        this.projects = this.tableDataTmp
      } else {
        this.currentPage = 1
        this.projects = this.tableDataTmp.filter(item =>
          // eslint-disable-next-line eqeqeq
          filters.status.some(ele => ele == item.status)
        )
      }
    },
    filterTag (value, row) {
      return row.status === value
    },
    handleCurrentChange (currentPage) {
      this.currentPage = currentPage
    },
    sortByDate (obj1, obj2, column) {
      var a = Date.parse(obj1.update_time)
      var b = Date.parse(obj2.update_time)
      if (a > b) {
        return -1
      } else {
        return 1
      }
    },
    // 获取全部项目
    getAllProjects () {
      var _this = this
      this.$axios
        .get('/project/mine', {
          params: {
            uid: _this.uid,
            career: _this.career
          }
        })
        .then(successResponse => {
          _this.projects = successResponse.data
          _this.tableDataTmp = successResponse.data
        })
        .catch(failResponse => {})
    }
  },
  created () {
    this.uid = this.$store.getters.uid
    this.career = this.$store.getters.career
    this.getAllProjects()
  }
}
</script>

<style lang="scss" scoped>
.project_table {
  padding-top: 0;
  margin: 10px 20px;
  position: relative;
  // margin-left: auto;
  // margin-right: auto;
}
.demo-table-expand {
  font-size: 0;
}
.demo-table-expand label {
  width: 90px;
  color: #99a9bf;
}
.demo-table-expand .el-form-item {
  margin-right: 0;
  margin-bottom: 0;
  width: 50%;
  color: red;
}
.pag {
  margin: 5px 70%;
}
</style>
