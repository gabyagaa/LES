from pyenergyplus.plugin import EnergyPlusPlugin

class LES_AC(EnergyPlusPlugin):

    def on_begin_zone_timestep_before_init_heat_balance(self, state):
       #SENSORES
        S_To = self.api.exchange.get_variable_handle(state, "Site Outdoor Air Drybulb Temperature", "Environment")
        V_To = self.api.exchange.get_variable_value(state, S_To)
        
        S_TZ_habitacion = self.api.exchange.get_variable_handle(state, "Zone Mean Air Temperature", "TZ_habitacion")
        V_TZ_habitacion = self.api.exchange.get_variable_value(state, S_TZ_habitacion)
        
        #ACTUADORES
        A_Tclima_cool = self.api.exchange.get_actuator_handle(state, "SCHEDULE:COMPACT", "SCHEDULE VALUE" , "Cooling")
        self.api.exchange.set_actuator_value(state, A_Tclima_cool, V_To)
        
        A_Tclima_hot = self.api.exchange.get_actuator_handle(state, "SCHEDULE:COMPACT", "SCHEDULE VALUE" , "Heating")
        self.api.exchange.set_actuator_value(state, A_Tclima_hot, V_To)
      
        A_Tguarda_cool = self.api.exchange.get_actuator_handle(state, "SCHEDULE:COMPACT", "SCHEDULE VALUE" , "Cooling_2")
        self.api.exchange.set_actuator_value(state, A_Tguarda_cool, V_TZ_habitacion)
        
        A_Tguarda_hot = self.api.exchange.get_actuator_handle(state, "SCHEDULE:COMPACT", "SCHEDULE VALUE" , "Heating_2")
        self.api.exchange.set_actuator_value(state, A_Tguarda_hot, V_TZ_habitacion)
        
      
        
        return 0
        
        