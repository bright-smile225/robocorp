import { RunInfo } from '~/lib';
import { Entry, EntryConsole } from '~/lib/types';

let callsToSetAllEntries:
  | {
      allEntries: Entry[];
      newExpanded: string[];
      consoleEntries: Entry[];
      updatedFromIndex: number;
    }
  | undefined;
let reactSetAllEntriesCallback: any;

/**
 * To be called from react to set the callback to be used to set the entries (should be called inside of useEffect()).
 */
export function reactCallSetAllEntriesCallback(setAllentriesCallback: any) {
  reactSetAllEntriesCallback = setAllentriesCallback;
  if (callsToSetAllEntries !== undefined) {
    setAllentriesCallback(
      callsToSetAllEntries.allEntries,
      callsToSetAllEntries.newExpanded,
      callsToSetAllEntries.consoleEntries,
      callsToSetAllEntries.updatedFromIndex,
    );
    callsToSetAllEntries = undefined;
  }
}

/**
 * Sets the entries. May be done right now if the react callback is already set or it may be
 * done at a later time (when the callback is actually set).
 */
export function setAllEntriesWhenPossible(
  allEntries: Entry[], // all the entries which should be set
  newExpanded: string[], // new entry ids to be expanded
  consoleEntries: EntryConsole[],
  updatedFromIndex = 0, // from which index onwards was there some change
) {
  if (reactSetAllEntriesCallback !== undefined) {
    reactSetAllEntriesCallback(allEntries, newExpanded, consoleEntries, updatedFromIndex);
  } else {
    if (callsToSetAllEntries !== undefined) {
      updatedFromIndex = Math.min(updatedFromIndex, callsToSetAllEntries.updatedFromIndex);
      newExpanded = callsToSetAllEntries.newExpanded.concat(newExpanded);
    }
    callsToSetAllEntries = { allEntries, newExpanded, consoleEntries, updatedFromIndex };
  }
}

let callsToSetRunInfo: { runInfo: RunInfo } | undefined;
let reactSetRunInfoCallback: any;

export function reactCallSetRunInfoCallback(setRunInfoCallback: any) {
  reactSetRunInfoCallback = setRunInfoCallback;
  if (callsToSetRunInfo !== undefined) {
    setRunInfoCallback(callsToSetRunInfo.runInfo);
    callsToSetRunInfo = undefined;
  }
}

export function setRunInfoWhenPossible(runInfo: RunInfo) {
  if (reactSetRunInfoCallback !== undefined) {
    reactSetRunInfoCallback(runInfo);
  } else {
    callsToSetRunInfo = { runInfo };
  }
}
