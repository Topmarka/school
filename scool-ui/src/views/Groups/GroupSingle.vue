<template>
  <div id="group-single">
    <navbar></navbar>
    <div class="step landing__section main-section past-events">
      <div class="page">
        <div class="container mt-1">
          <div class="page__inner">
            <profile-menu :header="header"></profile-menu>
            <div class="page__main" v-if="responseData">
              <div class="row">
                <div class="col-md-12">
                  <group-search></group-search>
                </div>
              </div>
              <single-group-header :group-name="responseData.name"></single-group-header>
              <hr/>
              <profiles-list :profiles="responseData.students"></profiles-list>
              <h6 v-if="responseData.students.length === 0" class="mt-5">Одногруппники отсутствуют</h6>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>


<script>
import Navbar from "../../components/Navbar";
import ProfileMenu from "../../components/Profile/ProfileMenu";
import GroupSearch from "../../components/Groups/GroupSearch";
import SingleGroupHeader from "../../components/Groups/SingleGroupHeader";
import ProfilesList from "../../components/Profile/ProfilesList";
import {requestsMixin} from "../../components/mixins/requestsMixin";
import {redirect} from "../../components/mixins/redirect";
import {friendMixin} from "../../components/mixins/friendMixin";

export default {
  title: 'Академия будущего | Личный кабинет',
  name: "GroupSingle",

  components: {
    Navbar, ProfileMenu, GroupSearch, SingleGroupHeader, ProfilesList,
  },

  data() {
    return {
      header: 'Группы'
    }
  },

  props: {
    id: String,
  },

  mixins: [requestsMixin, redirect, friendMixin],

  created() {
    this.createGetRequest(`/groups/${this.id}/`)
  },
}
</script>


<style scoped>

</style>